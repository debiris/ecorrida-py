from flask import request, jsonify
from config import app, db, bcrypt, jwt
from models import User
from flask_jwt_extended import create_access_token
from flask_cors import CORS

# Configurar CORS
CORS(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Verificar a força da senha
    if len(data['password']) < 8:
        return jsonify(message="A senha deve ter pelo menos 8 caracteres"), 400

    # Hash da senha usando bcrypt
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Criação do usuário com os novos campos
    new_user = User(
        firstname=data['firstname'],
        lastname=data['lastname'],
        username=data['username'],
        email=data['email'],
        age=data['age'],
        password=hashed_password,
        education_level=data['educationLevel'],
        gender=data['gender']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="Usuário criado com sucesso"), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'email': user.email})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Credenciais inválidas"), 401

if __name__ == '__main__':
    app.run(debug=True)
