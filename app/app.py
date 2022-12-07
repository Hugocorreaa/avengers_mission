from flask import Flask, render_template, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from service.marvel import herois

import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2315@localhost/heros'


# $ python
# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()


db = SQLAlchemy(app)

# Data Tables
class Hero(db.Model):
    id = db.Column(db.String, primary_key= True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    image = db.Column(db.Text)
    
    def _init_ (self, id, name, description, image):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
    
    def to_json(self):
        return {"id": self.id, "name": self.name, "description": self.description  , "image": self.image}
    
# MAIN ROUTE
@app.route("/")
def index():
    return render_template('index.html')

# ALL HEROS ROUTE
@app.route("/heros/", methods = ['GET', 'POST'])
def heros():
    if request.method == 'POST':
        lista_herois = herois(request.form['name'])
        return render_template('heros.html', lista_herois=lista_herois)
    else:
        lista_herois = herois(None)
        return render_template('heros.html', lista_herois=lista_herois)

# CHOSEN HEROS ROUTE
@app.route("/chosen", methods = ["GET", "POST"])
def chosen_heros():
    heros_objects = Hero.query.all()
    heros_json = [hero.to_json() for hero in heros_objects]
    
    if request.method == 'POST':
        body = request.json
        try:
            hero_info = Hero(id=body["id"], name=body["name"], description=body["description"], image=body["image"])
            db.session.add(hero_info)
            db.session.commit()
            return response(201, "heros", heros_json)
        except Exception as e:
            print(e)
            return response(400, 'heros', {}, "ERROR TO CHOOSE")  
    return render_template('chosen.html', heros_json=heros_json )

# DELETE CHOSEN HEROS
@app.route("/chosen/<id>", methods = ["POST"])
def delete_hero(id):
    hero_object = Hero.query.filter_by(id=id).first()
    try:
        db.session.delete(hero_object)
        db.session.commit()
        return response(200, "hero", {}, "DELETED SUCCESS")
    except Exception as e:
        print('Erro', e)
        return response(400, "hero", {}, "Error to delete")


def response(status, content_name, content, mesage=False):
    body = {}
    body[content_name] = content
    
    if(mesage):
        body["mesage"] = mesage
    
    return Response(json.dumps(body), status=status, mimetype="application/json")
    
    
if __name__ == '__main__':
    app.run(debug=True)