from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Estilo do Rei Barbearia"

@app.route('/novofuncionario')
def adicionar_funcionario():
    return "funcionário adicionado"

app.run(debug=True)

