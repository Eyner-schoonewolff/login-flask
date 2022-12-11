from database.db import db,ma

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    contraseña = db.Column(db.String(50), nullable=False)
    nombre=db.Column(db.String(20))

    def __init__(self, email, contraseña,nombre):
        self.email = email
        self.contraseña = contraseña
        self.nombre=nombre

class Esquema_usuario(ma.Schema):
    class Meta:
        fields=('id','email','contraseña','nombre')


usaurio_esquema=Esquema_usuario()
usaurios_esquema=Esquema_usuario(many=True)