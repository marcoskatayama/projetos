from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MINHA PALAVRA SECRETA'

from app import routes