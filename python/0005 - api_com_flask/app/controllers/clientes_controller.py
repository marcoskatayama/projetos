# app/controllers/clientes_controller.py
from flask import Blueprint, make_response, jsonify, request
from app.models.clientes import Clientes

clientes_bp = Blueprint('clientes', __name__)


# Rota para obter todos os clientes
@clientes_bp.route('/', methods=['GET'])
def get_clientes():
    # Lógica para obter todos os clientes
    return make_response(
        jsonify(Clientes)
        )
    pass


# Rota para obter cliente por id
@clientes_bp.route('/<int:id>', methods=['GET'])
def get_carro(id):
    # Lógica para obter um cliente pelo ID
    for cliente in Clientes:
        if cliente.get('id') == id:
            return make_response(jsonify(cliente))
    pass


# Rota para criar um novo cliente
@clientes_bp.route('/', methods=['POST'])
def create_carro():
    # Lógica para criar um novo cliente
    cliente = request.json
    Clientes.append(cliente)
    return jsonify(cliente), 201
    pass


# Rota para atualizar um cliente existente
@clientes_bp.route('/<int:id>', methods=['PUT'])
def update_carro(id):
    # Lógica para atualizar um cliente existente
    carro_atualizado = request.json
    for cliente in Clientes:
        if cliente.get('id') == id:
            Clientes.update(carro_atualizado)
            return jsonify(cliente), 200
    return jsonify({"error": "cliente não encontrado"}), 404


# Rota para excluir um cliente
@clientes_bp.route('/<int:id>', methods=['DELETE'])
def delete_carro(id):
    # Lógica para excluir um cliente existente
    for cliente in Clientes:
        if cliente.get('id') == id:
            Clientes.remove(cliente)
            return jsonify({"message": "cliente excluído com sucesso"}), 204
    return jsonify({"error": "cliente não encontrado"}), 404
    pass
