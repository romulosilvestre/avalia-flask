from flask import Flask,render_template,request,redirect, session,url_for,flash
from usuario import Usuario
app = Flask(__name__)

app.secret_key = 'supersecretkey'  # Substitua por uma chave secreta real


usuario1 = Usuario("bruno", "BD", "123")
usuario2 = Usuario("camila", "Mila", "paozinho")
usuario3 = Usuario("guilherme", "Cake", "python_eh_vida")

usuarios = { usuario1.nome : usuario1,
             usuario2.nome : usuario2,
             usuario3.nome: usuario3 }




@app.route('/')
def index():
    return render_template('index.html')

"""
versão antiga para estudo
@app.route('/autenticar',methods=['POST','GET'])
def autenticar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        if request.form['senha'] == 'senac' and usuario == 'walter':
          session['usuario_logado'] = usuario
          return render_template('agendamento.html')
        else:
           return 'erro na autenticacao'

"""
# definir a rota autenticar
@app.route('/autenticar', methods=['POST',])
def autenticar(): # criei uma função autenticar

 
    
    if request.form['usuario'] in usuarios: #verifico no dicionário se existe esse usuário
        usuario = usuarios[request.form['usuario']] # usuário recebe o valor do html
        if request.form['senha'] == usuario.senha: # se a senha do html for igual do dicionário
            session['usuario_logado'] = usuario.nickname # então o nickname será armazenado nos cookies
            #flash(usuario.nickname + ' logado com sucesso!')
            return "LOGADO"
    else:
        flash('Usuário não logado.')
        return "usuario não logado"


@app.route('/logout')
def sair():
    session.pop('usuario_logado', None)
    return redirect(url_for('index'))

app.run(debug=True)











"""
@app.route('/novofuncionario')
def adicionar_funcionario():
    return "funcionário adicionado"

@app.route('/login',methods=['GET', 'POST'])
def logar():
     if request.method == 'POST':
       session['email'] = request.form['email']
       if session['email'] == 'joao@gmail.com':
         return redirect(url_for('agendar'))

@app.route('/novocliente')
def novo_cliente():
      if 'email' in session:
        return f'Logged in as {session["email"]}'
      return 'You are not logged in'

@app.route('/novoagendamento')
def agendar():
    email = session.get('email')
    if not email:
        return redirect(url_for('login'))
    return render_template('agendamento.html', email=email)
"""