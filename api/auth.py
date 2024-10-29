from flask import Blueprint, abort, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from maps.schemas.member import MemberTokenData
from maps.schemas.response import response_data
from maps.services.auth import check_password, get_user_by_userid
from maps.services.token import create_token_data, refresh_token_data


auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

# 폴더 경로 설정 (업로드된 파일을 저장할 위치)
@auth_blueprint.route("/", methods=["GET"])
def get_auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        abort(401)
        
    member_data = get_user_by_userid(auth.username)
    if not member_data:
        abort(401)
    
    result = check_password(encrypted_password=auth.password, hash_password=member_data.userpw)
    if not result:
        abort(401)
    
    token_data = create_token_data(member_data)

    return response_data(message='Login', data=token_data.model_dump())


@auth_blueprint.route('/token', methods=['GET'])
@jwt_required(refresh=True)
def get_token():
    member_token_data = MemberTokenData.model_validate(get_jwt_identity())
    token_data = refresh_token_data(member_token_data)
    return response_data(message='Token.....', data=token_data.model_dump())



