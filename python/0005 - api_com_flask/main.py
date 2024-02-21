from flask import Flask
from app.controllers.carros_controller import carros_bp
from app.controllers.clientes_controller import clientes_bp


app = Flask(__name__)

# Flaks ordena o json do response em ordem alfabetica por padrão,
app.config['JSON_SORT_KEYS'] = False

# Registrar blueprints
app.register_blueprint(carros_bp, url_prefix='/carros')
app.register_blueprint(clientes_bp, url_prefix='/clientes')

if __name__ == '__main__':
    app.run()
