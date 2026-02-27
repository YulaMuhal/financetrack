from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas na base de dados
    app.run(debug=True)