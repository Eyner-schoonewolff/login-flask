from flask import Blueprint, render_template, redirect, url_for, request, url_for, session
from router.verificacion.verificacion_login import Verificacion
from flask_login import logout_user, LoginManager

login = Blueprint("login", __name__, template_folder='../vistas',
                  static_folder='../vistas/archivos')

login_manager = LoginManager()
login_manager.login_view = 'login'
verificacion = Verificacion()


@login.route("/")
def index():
    try:
        logueado = session['loggin']
        if logueado:
            return redirect(url_for("login.home"))  # /home
        return redirect(url_for("login.inicio"))  # /login
    except KeyError:
        return redirect(url_for("login.inicio"))  # /login



@login.route("/login", methods=["GET"])
def inicio():
    try:
        logueado = session['loggin']
        if logueado:
            return redirect(url_for("login.home"))
        return render_template("index.html")
    except:
        return render_template("index.html")


@login.route("/auth", methods=['GET', 'POST'])
def auth():
    if not request.method == 'POST':
        return render_template('index.html')

    if not verificacion.email_y_contraseña_verificacion():
        return {"login": False, "home": '/'}

    if not verificacion.email_verificacion():
        return {"login": False, "home": '/'}

    if not verificacion.contraseña_verificacion():
        return {"login": False, "home": '/'}

    nombre = verificacion.obtener_usuario()
    session['nombre'] = nombre
    session['loggin'] = True
    return {'login': True, 'home': '/inicio'}


@login.route('/logout')
@login_manager.user_loader
def logout():
    logout_user()
    session['loggin'] = False
    return redirect(url_for('login.inicio'))


@login.route("/inicio", methods=['GET'])
def home():
    try:
        logueado = session['loggin']
        if logueado:
            nombre = session['nombre']
            return render_template("inicio.html", nombre=nombre)
        else:
            return redirect(url_for("login.inicio"))
    except:
        return redirect(url_for("login.inicio"))