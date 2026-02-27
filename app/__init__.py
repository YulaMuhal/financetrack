from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Instâncias globais
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    login_manager.init_app(app)

    # Regista as rotas
    from app.routes.auth import auth
    from app.routes.dashboard import dashboard
    from app.routes.transations import transations
    from app.routes.category import category

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(transations)
    app.register_blueprint(category)

    return app