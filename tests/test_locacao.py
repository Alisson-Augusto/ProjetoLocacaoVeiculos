from typing import List
from flask import Flask
import pytest
from app import create_app
from app import db
from app.models.agencia import Agencia
from app.models.recibo import Recibo
from app.models.usuario import Usuario
from app.models.veiculos import Veiculos

NOME = "Teste"
EMAIL = "teste@gmail.com"
SENHA = "senha_teste"

@pytest.fixture
def app():
  app = create_app("test")

  # Remove todos os dados anteriores
  with app.app_context():
    db.drop_all()
    db.create_all()

    # Loga usuário para testar rotas onde é necessário login
    with app.test_client() as client:
      logar(client)

    criar_agencias(db.session, 5)
    yield app

  # Remove todos os dados inseridos após os testes
  with app.app_context():
    db.drop_all()


def logar(client):
  usuario = Usuario(nome=NOME,
                    email=EMAIL,
                    senha=SENHA,
                    data_nascimento="2001-05-19")
  
  db.session.add(usuario)
  response = client.post("/login", data={
        "email": EMAIL,
        "senha": SENHA,
  })

  assert response.status_code == 302
  

def test_escolha_veiculos(app: Flask):
  '''
    Testa se a exibição dos veículos dada uma agência, 
    esta correta, de forma que apenas veículos disponíveis e 
    atualmente na agência sejam visíveis.
  '''
  agencia = Agencia.query.first()

  with app.test_client() as client:
    response = client.get(f"/agencias/{agencia.id}")
    assert response.status_code == 200
    assert all([veiculo.get_nome() in str(response.data) for veiculo in agencia.veiculos])


def test_gerar_recibo_e_perfil_do_usuario(app: Flask):
  '''
    Testa se o recibo esta sendo gerado corretamente,
    de acordo com as informações respondidas no formulário
    de locação. Também valida se na rota "/conta" as informações sobre
    o veículo reservado, esta sendo exibido corretamente.
  '''

  ag_retirada = Agencia.query.first()
  veiculo = ag_retirada.veiculos[0]
  data_retirada  = "2023-05-19"
  data_devolucao = "2023-05-21"
  with app.test_client() as client:
    response = client.post(f"/agencias/{ag_retirada.id}", data={
          "ag_retirada" : ag_retirada.id,
          "data_retirada": data_retirada,
          "ag_devolucao": ag_retirada.id,
          "data_devolucao": data_devolucao,
          "veiculo": veiculo.id
      })

    # Valida se a requisição enviou código de status de redirect (302)
    # Indicando que formulário foi processado com sucesso
    # e usuário retornou para página inicial "/"
    assert response.status_code == 302

    # Verifica se o recibo foi registrado
    assert len(Recibo.query.filter(Recibo.veiculo==veiculo.id).all()) == 1

    # Verfica se reserva esta sendo exibido no perfil do usuário
    response = client.get("/conta")
    assert veiculo.get_nome() in str(response.data)


def criar_agencias(db_session, total_agencias):
  # Adiciona veículos e agências para teste
  veiculos_por_agencia = criar_veiculos(total_agencias)
  agencia_id = 1
  for veiculos in veiculos_por_agencia:
    agencia = Agencia(
          id=agencia_id,
          localizacao=f"Localização agência {agencia_id}",
          nome=f"Agência {agencia_id}")
    
    for veiculo in veiculos:
      agencia.veiculos.append(veiculo)
      db_session.add(veiculo)

    db_session.add(agencia)
    agencia_id += 1

  db_session.commit()


def criar_veiculos(total_agencias) -> List[List[Veiculos]]:
  veiculos_por_agencia = []
  veiculo_id = 0
  for j in range(total_agencias):
    # Cria 5 veículos para cada agência
    veiculos = []
    for i in range(5):
      veiculo = Veiculos(
          diaria=100,
          descricao=f"Veiculo {veiculo_id}",
          imagem=f"imagem_{veiculo_id}.jpg",
          modelo=f"Modelo {veiculo_id}",
          marca=f"Marca {veiculo_id}",
          placa=f"PLACA{veiculo_id}",
          ocupantes=5,
          porta_malas=2,
          freio_abs=True,
          disponibilidade=True
      )
      veiculos.append(veiculo)
      veiculo_id += 1
    
    veiculos_por_agencia.append(veiculos)

  return veiculos_por_agencia
