from flask import Flask,render_template,request,redirect, session,url_for


app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Substitua por uma chave secreta real

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/logout')
def sair():
    session.pop('email', None)
    return redirect(url_for('index'))

app.run(debug=True)

