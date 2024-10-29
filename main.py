from flask import Blueprint

from maps.schemas.response import response_data
from maps.api.auth import auth_blueprint
from maps.api.rsa import rsa_blueprint

maps_blueprint = Blueprint('maps', __name__, url_prefix='/maps')
maps_blueprint.register_blueprint(auth_blueprint)
maps_blueprint.register_blueprint(rsa_blueprint)


@maps_blueprint.route('/', methods=['GET'])
def start():
    return response_data(data='Welcome to MAPS')
    