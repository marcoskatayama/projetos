from app import app
from flask import render_template, request, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuario', defaults={'nome':'usuário'})
@app.route('/usuario/<nome>')
def usuario(nome):
    dados = {'Profissão':'Desenvolvedor', 'Cidade': 'Maringá', 'UF': 'PR'}
    return render_template('usuario.html', nome=nome, dados=dados)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return 'usuário: {} e senha: {}'.format(usuario,senha)

@app.route('/autenticarviapost', methods=['POST'])
def autenticarviapost():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == 'admin' and senha== '123':
        return 'usuário: {} e senha: {}'.format(usuario,senha)
    else:
        flash('Dados inválidos!')
        return redirect('/login')
    