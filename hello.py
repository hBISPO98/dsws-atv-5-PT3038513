# Importações de bibliotecas e ferramentas necessárias
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Inicialização de Flask e definição de chave secreta
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chave Forte'

bootstrap = Bootstrap(app)

# Criação do formulário e suas definições
class NameForm(FlaskForm):
    name = StringField('Qual é o seu nome?', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# Rota função view
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data # variável de sessão
        return redirect(url_for('index'))
    # Renderiza a página HTML com os dados salvos na session
    return render_template('index.html', form=form, name=session.get('name'))

# Rotas de erro
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500