import json
from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def home():

    projetos_brutos = []

    try:
        with open('projetos.json', 'r', encoding='utf-8') as card_projetos:
            projetos_brutos = json.load(card_projetos)
    except Exception as e:
        projetos_brutos = []
        print('Erro no banco de dados! Tentando novamente...')

    return render_template('index.html', projetos_brutos=projetos_brutos)
        

if __name__ == '__main__':
    app.run(debug=True)