# app/controllers/carros_controller.py
from flask import Blueprint, make_response, jsonify, request
from app.models.carros import Carros

carros_bp = Blueprint('carros', __name__)


# Rota para obter todos os carros
@carros_bp.route('/', methods=['GET'])
def get_carros():
    # Lógica para obter todos os carros
    print('1')
    return make_response(
        jsonify(Carros)
        )


# Rota para obter carro por id
@carros_bp.route('/<int:id>', methods=['GET'])
def get_carro(id):
    # Lógica para obter um carro pelo ID
    for carro in Carros:
        if carro.get('id') == id:
            return make_response(jsonify(carro))
    pass


# Rota para criar um novo carro
@carros_bp.route('/', methods=['POST'])
def create_carro():
    # Lógica para criar um novo carro
    carro = request.json
    Carros.append(carro)
    return jsonify(carro), 201


# Rota para atualizar um carro existente
@carros_bp.route('/<int:id>', methods=['PUT'])
def update_carro(id):
    # Lógica para atualizar um carro existente
    carro_atualizado = request.json
    for carro in Carros:
        if carro.get('id') == id:
            carro.update(carro_atualizado)
            return jsonify(carro), 200
    return jsonify({"error": "Carro não encontrado"}), 404


# Rota para excluir um carro
@carros_bp.route('/<int:id>', methods=['DELETE'])
def delete_carro(id):
    # Lógica para excluir um carro existente
    for carro in Carros:
        if carro.get('id') == id:
            Carros.remove(carro)
            return jsonify({"message": "Carro excluído com sucesso"}), 204
    return jsonify({"error": "Carro não encontrado"}), 404
