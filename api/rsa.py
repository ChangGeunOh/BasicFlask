from flask import Blueprint, request

from maps.models.key_store import KeyStore
from maps.schemas.response import response_data
from maps.services.auth import generate_or_update_key


rsa_blueprint = Blueprint('rsa', __name__, url_prefix='/rsa')

@rsa_blueprint.route('/', methods=['GET'])
def get_rsa():
    public_key = generate_or_update_key()
    return response_data(message='GET RSA', data=public_key)