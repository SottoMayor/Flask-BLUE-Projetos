from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():

    enimies_list = [
        {"imgPath": "../static/images/csgo-phoenix-tr.png",
         "alt": "Terrorist Phoenix", "description": "Terrorista Phoenix"},
        {"imgPath": "../static/images/csgo-elite-crew-tr.png",
         "alt": "Terrorist Elit Crew", "description": "Terrorista Elit Crew"},
        {"imgPath": "../static/images/csgo-separatist-tr.png",
         "alt": "Terrorist Separatist", "description": "Terrorista Separatist"}
    ]

    guns_list = [
        {"imgPath": "../static/images/csgo-deagle.png",
            "alt": "Desert Eagle", "description": "Desert Eagle"},
        {"imgPath": "../static/images/csgo-ak47.jpg",
            "alt": "AK47", "description": "Ak47"},
        {"imgPath": "../static/images/csgo-awp.png",
            "alt": "AWP", "description": "AWP"},
    ]

    return render_template(
        'index.html', enimies_list, guns_list)


if __name__ == '__main__':
    app.run(debug=True)
