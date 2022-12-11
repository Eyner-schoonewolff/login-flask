from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from router.login_router import login

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:@localhost/logjn"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config['SECRET_KEY'] ='codgio_secreto'


SQLAlchemy(app)
LoginManager(app)

app.register_blueprint(login)