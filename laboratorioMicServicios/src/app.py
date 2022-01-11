from flask             import Flask, request, jsonify
from flask_sqlalchemy  import SQLAlchemy
from flask_marshmallow import Marshmallow

import json


with open('../secret.json') as file:
    data_bd = json.load(file)

CADENA_CONEXION_BD = 'mysql+pymysql://{}:{}@localhost/bdprueba'.format(data_bd['USERBD'],data_bd['PASSBD'])
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CADENA_CONEXION_BD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Producto(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    nombre   = db.Column(db.String(50), unique=True)
    precio   = db.Column(db.Float)
    cantidad = db.Column(db.Integer) 

    def __init__(self, nombre, precio, cantidad):
        self.nombre   = nombre
        self.precio   = precio
        self.cantidad = cantidad


db.create_all()


class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'precio', 'cantidad')


producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)


@app.route('/productos/crear-producto', methods=['POST'])
def crear_poducto():
    nombre   = request.json['nombre']
    precio   = request.json['precio']
    cantidad = request.json['cantidad']

    producto_nuevo = Producto(nombre, precio, cantidad)

    db.session.add(producto_nuevo)
    db.session.commit()

    resultado = producto_schema.jsonify(producto_nuevo)
    
    return resultado


if __name__ == '__main__':
    PORT = 5000
    app.run(debug=True, port=PORT)