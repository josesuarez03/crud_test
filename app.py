from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cabra.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definición del modelo para la cabra con características adicionales
class Cabra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    raza = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    peso = db.Column(db.Float, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    produce_leche = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'edad': self.edad,
            'raza': self.raza,
            'color': self.color,
            'peso': self.peso,
            'altura': self.altura,
            'produce_leche': self.produce_leche
        }

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

# Ruta para crear una nueva cabra (CREATE)
@app.route('/cabra', methods=['POST'])
def crear_cabra():
    data = request.json
    nueva_cabra = Cabra(
        nombre=data['nombre'],
        edad=data['edad'],
        raza=data['raza'],
        color=data['color'],
        peso=data['peso'],
        altura=data['altura'],
        produce_leche=data['produce_leche']
    )
    db.session.add(nueva_cabra)
    db.session.commit()
    return jsonify(nueva_cabra.to_dict()), 201

# Ruta para obtener todas las cabras (READ)
@app.route('/cabra', methods=['GET'])
def obtener_cabras():
    cabras = Cabra.query.all()
    return jsonify([cabra.to_dict() for cabra in cabras]), 200

# Ruta para obtener una cabra específica por ID (READ)
@app.route('/cabra/<int:id>', methods=['GET'])
def obtener_cabra(id):
    cabra = Cabra.query.get_or_404(id)
    return jsonify(cabra.to_dict()), 200

# Ruta para actualizar una cabra (UPDATE)
@app.route('/cabra/<int:id>', methods=['PUT'])
def actualizar_cabra(id):
    data = request.json
    cabra = Cabra.query.get_or_404(id)

    cabra.nombre = data.get('nombre', cabra.nombre)
    cabra.edad = data.get('edad', cabra.edad)
    cabra.raza = data.get('raza', cabra.raza)
    cabra.color = data.get('color', cabra.color)
    cabra.peso = data.get('peso', cabra.peso)
    cabra.altura = data.get('altura', cabra.altura)
    cabra.produce_leche = data.get('produce_leche', cabra.produce_leche)

    db.session.commit()
    return jsonify(cabra.to_dict()), 200

# Ruta para eliminar una cabra (DELETE)
@app.route('/cabra/<int:id>', methods=['DELETE'])
def eliminar_cabra(id):
    cabra = Cabra.query.get_or_404(id)
    db.session.delete(cabra)
    db.session.commit()
    return jsonify({"mensaje": f"La cabra con ID {id} ha sido eliminada."}), 200

# Correr la aplicación
if __name__ == '__main__':
    app.run(debug=True)
