from flask import (Flask, Blueprint, render_template)

app = Flask(__name__)
bp = Blueprint('app', __name__)

filmes = [
    {
        "id": 1,
        "nome": "Harry Potter e a Pedra Filosofal",
        "imagem_url": "https://ingresso-a.akamaihd.net/img/cinema/cartaz/7766-cartaz.jpg"
    },
    {
        "id": 2,
        "nome": "Senhor dos Anéis: As Duas Torres",
        "imagem_url": "https://i.pinimg.com/originals/e5/e8/cf/e5e8cfc267a11c8ae6ba728b4537543f.jpg"
    },
    {
      "id": 3,
      "nome": "The Matrix",
      "imagem_url": "https://br.web.img3.acsta.net/c_310_420/medias/nmedia/18/91/08/82/20128877.JPG"
    }
]

@bp.route('/')
def home():
  return render_template('index.html')

@bp.route('/read')
def listar_filmes():
  return render_template('listar-filmes.html', listaDeFilmes=filmes) # Passando para dentro do nosso HTML os dados da minha listagem de filmes!!!!

@bp.route('/read/<id_filme>')
def lista_detalhe_filme(id_filme):
  return 'Página em Construção para o filme com ID -> ' + id_filme

# Pega os dados do blueprint da nossa aplicação (nome do app e as rotas) e registra dentro do app do Flask
app.register_blueprint(bp)

if __name__ == '__main__':
  app.run(debug=True)
