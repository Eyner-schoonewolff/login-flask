from modelos.usuarios import Usuario, usaurios_esquema,usaurio_esquema
from router.verificacion.request_email import request_email,request_contraseña

class Verificacion:
    def email_verificacion(self):
        query_usuarios = Usuario.query.all()
        usuarios = usaurios_esquema.dump(query_usuarios)
        email = request_email()

        for usuario in usuarios:
            if usuario['email'] == email:
                return True
        return False

    def contraseña_verificacion(self):
        query_usuarios = Usuario.query.all()
        usuarios = usaurios_esquema.dump(query_usuarios)
        contraseña = request_contraseña()
        for usuario in usuarios:
            if usuario['contraseña'] == contraseña:
                return True
        return False

    def email_y_contraseña_verificacion(self):
        query_usuarios = Usuario.query.all()
        usuarios = usaurios_esquema.dump(query_usuarios)
        email = request_email()
        contraseña = request_contraseña()
        for usuario in usuarios:
            if usuario['email'] == email and usuario['contraseña'] == contraseña:
                return True
        return False

    def obtener_usuario(self):
        email = request_email()
        if email is None:
            return email
     
        query_usuario = Usuario.query.filter_by(email=email).first()
    
        nombre=usaurio_esquema.dump(query_usuario)['nombre']

        return nombre
