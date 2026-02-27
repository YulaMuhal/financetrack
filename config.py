import os

class Config:
    # Chave secreta para sessões e segurança
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-dev-123'
    
    # Base de dados
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'financetrack.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False