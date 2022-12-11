from flask import request

def request_email():
    usuario=request.get_json(force=False, silent=False, cache=True)
    email= usuario['email']
    return email

def request_contraseña():
    usuario=request.get_json()
    contraseña= usuario['contraseña']
    return contraseña
