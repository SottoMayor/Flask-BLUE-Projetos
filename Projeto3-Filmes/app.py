from flask import (Flask, Blueprint, render_template)

app = Flask(__name__)
bp = Blueprint('app', __name__)

filmes = []


@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/read')
def listar_filmes():
    # Passando para dentro do nosso HTML os dados da minha listagem de filmes!
    return render_template('listar-filmes.html', listaDeFilmes=filmes)


@bp.route('/read/<id_filme>')
def lista_detalhe_filme(id_filme):
    return 'Página em Construção para o filme com ID -> ' + id_filme


# Pega os dados do blueprint da nossa aplicação (nome do app e as rotas) e 
# registra dentro do app do Flask
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
