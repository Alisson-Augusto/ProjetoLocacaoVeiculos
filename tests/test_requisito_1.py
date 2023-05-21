import pytest
from app import create_app
from app import db
from app.models.usuario import Usuario

@pytest.fixture
def client():
  app = create_app("test")

  # Remove todos os dados anteriores
  with app.app_context():
    db.drop_all()
    db.create_all()
  
  with app.test_client() as client:
    yield client
  
  # Remove todos os dados inseridos após os testes
  with app.app_context():
    db.drop_all()


def test_cadastro_e_login_usuario(client):
  response = client.post("/cadastro", data={
        "nome" : "TestUser",
        "email": "test@exemplo.com",
        "senha": "TestSenha",
        "data_nascimento": "2001-05-19"
    })

  # Valida se o código de status da requisição é de redirect 302
  # Indicando que usuário foi cadastrado com sucesso e
  # foi direcionado para a página inicial "/"
  assert response.status_code == 302

  # Testa Login, com o novo usuário registrado
  response = client.post("/login", data={
        "email": "test@exemplo.com",
        "senha": "TestSenha",
    })

  assert response.status_code == 302
  