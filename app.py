from flask import Flask, render_template
from service.marvel import herois



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/heros")
def heros():
    lista_herois = herois()
    return render_template('heros.html', listaHerois=lista_herois)


    

if __name__ == '__main__':
    app.run(debug=True)