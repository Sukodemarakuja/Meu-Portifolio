from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def home():
    # Uma lista de projetos reais (dados simulando um banco de dados)
    meus_projetos = [
        {
            "titulo": "Este meu Portfólio",
            "descricao": "Criado usando Flask para servir páginas dinâmicas, com estilos modernos em CSS.",
            "link": "#"
        },
        {
            "titulo": "Scripts de Automação",
            "descricao": "Conjunto de scripts em Python desenvolvidos para automatizar tarefas cotidianas.",
            "link": "https://github.com/sukodemarakuja"
        }
    ]
    
    return render_template('index.html', projetos=meus_projetos)

@app.route('/contato')
def contato():
    return "<h1> Caso queira entrar em contato comigo, envie um email para: <p> <strong>jaohenrick04@gmail.com</strong> </p> </h1>"

if __name__ == '__main__':
    app.run(debug=True)