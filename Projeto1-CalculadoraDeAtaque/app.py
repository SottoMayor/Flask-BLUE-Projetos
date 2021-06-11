from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():

    return render_template(
        'index.html',
        name='Messão',
        hp=1200,
        gif_url='https://media4.giphy.com/media/loG32MXYyQl5vUJL46/200w.' +
        'gif?cid=82a1493betw1h7mnltat4ikehke0m61v0l8fp1dfy64ssg5c&rid=' +
        '200w.gif&ct=g')


if __name__ == '__main__':
    app.run(debug=True)
