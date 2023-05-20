# Rotas

## Requisito 1: O sistema deve permitir que os usuários criem uma conta e façam login.

## Implementação do Requisito:
Foi criado duas rotas `/login` e `/cadastro` definidos no arquivo `app/autenticacao.py`.

Na rota `/login`: Página renderiza formulário de login para usuaŕio e permite autenticação, caso usuário informe as credenciais correspondentes as fornecidas durante preenchimento do formulário da rota de `/cadastro`.

A rota de login é definida no arquivo `app/autenticacao.py`
```py
@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        usuario:Usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verificar_senha(form.senha.data):
            login_user(usuario)
            return redirect("/")
        flash("Email ou senha incorreto")

    return render_template("auth/login.html", form=form)
```

Rota de Cadastro também é definida no mesmo arquivo
```py
@auth.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        email = form.email.data
        usuario:Usuario = Usuario.query.filter_by(email=email).first()
        if not usuario:
            # Registra usuário no banco
            user = Usuario(
                nome=form.nome.data,
                email=email,
                senha=form.senha.data,
                data_nascimento=form.data_nascimento.data
                )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect("/")
        
        flash("Este usuário já foi cadastrado")
    return render_template("auth/cadastro.html", form=form)
```

Tanto o login quanto cadastro possuem classes `LoginForm` e `CadastroForm`, nas quais são implementadas as validações do "lado do servidor" por meio da biblioteca Flask-WTF por meio dos arquivos `app/forms/login.py` e `app/forms/cadastro.py`, para garantir que as informações de cadastro não são nulas.


classes LoginForm e CadastroForm
```py
class LoginForm(FlaskForm):
    email = EmailField("email", validators=[InputRequired()])
    senha = PasswordField("senha", validators=[InputRequired()])

class CadastroForm(FlaskForm):
    nome = StringField('nome', validators=[InputRequired()])
    email = EmailField("email", validators=[InputRequired()])
    senha = PasswordField("senha", validators=[InputRequired()])
    data_nascimento = DateField("data_nascimento", validators= InputRequired()])
```

## Teste do Requisito:
O Arquivo `tests/test_requisito_1.py` garante que este requisito esta funcionando corretamente, pois meio da definição

```py
@pytest.fixture
def client():
  app = create_app("test")

  with app.app_context():
    db.drop_all()
    db.create_all()
  
  with app.test_client() as client:
    yield client
```

É declarado para create_app utilizar a configuração de teste, isso implica que, o banco utilizado será o de teste, portanto. Não impactará os bancos de Produção e Desenvolvimento.

Para garantir que o requisito 1 seja atendido, é definido a seguinte função de teste

```py
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
```
