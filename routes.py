from flask import Blueprint 

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def home():
    return "Olá, Mundo!"