from src.app import app
from database.db import db
from router.login_router import login_manager

login_manager.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.secret_key='codgio_secreto'
    app.run(debug=True)

