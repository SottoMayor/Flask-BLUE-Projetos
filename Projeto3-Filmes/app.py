from flask import (Flask, Blueprint, render_template)
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
bp = Blueprint('app', __name__)


# Conectando com o banco de dados
user = 'zkcsyvoy'
password = '9Mtctta5J_Rs98ORf1i8Mxl2PtVUwF2W'
hostname = 'tuffi.db.elephantsql.com'
database = 'zkcsyvoy'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:' + \
    f'{password}@{hostname}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Filmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, image_url):
        self.nome = nome
        self.image_url = image_url

    @staticmethod
    def read_all():
        # Buscando todos os filmes do DB
        return Filmes.query.all()

    @staticmethod
    def read_single(filme_id):
        return Filmes.query.get(filme_id)


@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/read')
def listar_filmes():
    # Passando para dentro do nosso HTML os dados da minha listagem de filmes!
    registros = Filmes.read_all()
    print(registros)
    return render_template('listar-filmes.html', registros=registros)


@bp.route('/read/<id_filme>')
def lista_detalhe_filme(id_filme):
    filme = Filmes.read_single(id_filme)
    return render_template('read-single.html', filme=filme)


# Pega os dados do blueprint da nossa aplicação (nome do app e as rotas) e
# registra dentro do app do Flask
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
