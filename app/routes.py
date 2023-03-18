from app import app
from flask import render_template


@app.route('/')
@app.route('/index')

def index():
    nome = 'Eliezio Loureiro'

    dados = {
        'Profissão' : 'Assitente',
        'Empresa' : 'Bemol'
    }
    return render_template('index.html', nome = nome, dados = dados) # chamando os arquivos em html 

@app.route('/contato')
def contato():
    return render_template('contato.html')