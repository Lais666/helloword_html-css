from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    texto = 'Hello World!'
    outrotexto = 'Bem-vindo à sua primeira página Flask!'
    return(render_template('index.html', texto = texto, outro = outrotexto))

from flask import Flask, render_template

if __name__ == '__main__':
    app.run(debug=True)
