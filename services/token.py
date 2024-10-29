
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token

from maps.schemas.member import MemberData, MemberTokenData
from maps.schemas.token import TokenData


ACCESS_EXPIRE_MINUTES_TIME = 10
REFRESH_EXPIRE_HOURS_TIIME   = 12


def create_token_data(memberData: MemberData) -> TokenData:
    member_token_data = MemberTokenData.model_validate(memberData.model_dump())
    access_token = create_access_token(identity=member_token_data.model_dump(), expires_delta=timedelta(minutes=ACCESS_EXPIRE_MINUTES_TIME))
    refresh_token = create_refresh_token(identity=member_token_data.model_dump(), expires_delta=timedelta(hours=REFRESH_EXPIRE_HOURS_TIIME))
    return  TokenData(access_token=access_token, refresh_token=refresh_token)

def refresh_token_data(member_token_data: MemberTokenData) -> TokenData:
    return TokenData(access_token=create_access_token(identity=member_token_data.model_dump(), expires_delta=timedelta(minutes=ACCESS_EXPIRE_MINUTES_TIME)))