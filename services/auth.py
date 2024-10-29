from pathlib import Path
import time
from typing import Optional
import bcrypt

from maps.models.key_store import KeyStore
from maps.models.member import Member
from maps.schemas.member import MemberData
from maps.config.logger import logger
from maps.services.rsa import rsa_decrypt, key_change_time_interval, generate_key
from maps.utils.utils import getCurrentTimeMils
from maps.config.database import db


UPLOAD_DIR = Path(__file__).parent / "../uploads/members"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def get_user_by_userid(userid: str) -> Optional[MemberData]:
    
    unit_member = Member.query.filter_by(userid=userid).first()
    if not unit_member:
        return None
    
    return MemberData.model_validate(unit_member)

def check_password(encrypted_password: str, hash_password: str) -> bool:
    private_key = get_private_key()

    if private_key:
        plain_password = rsa_decrypt(private_key, encrypted_password)
        logger.info(f'PLAIN PASSWORD : {plain_password}')
        logger.info(f'ENCRYPTED PASSWORD : {encrypted_password}')
        # if verify_password(plain_password, hash_password):
        #     logger.info(f'Success: {verify_password(plain_password=plain_password, hashed_password=hash_password)}')
        # else:
        #     logger.info(f'FAIL   : {verify_password(plain_password=plain_password, hashed_password=hash_password)}')
    
    return verify_password(plain_password=plain_password, hashed_password=hash_password if private_key else False)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Compare the provided plain password with the hashed password from the database
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


is_processing = False

def generate_or_update_key():
    """
    키가 없거나, 갱신이 필요하면 키를 새로 생성하고 저장합니다.
    """
    global is_processing

    # 키가 이미 존재하는지 확인
    key_obj = KeyStore.query.first()
    if key_obj:
        key_change_time = key_obj.key_timestamp
        public_key = key_obj.pub_key
        private_key = key_obj.priv_key
    else:
        key_change_time = None
        public_key = None
        private_key = None

    current_time = getCurrentTimeMils()

    # 키가 없거나, 갱신 주기가 지난 경우 새로운 키를 생성
    if not key_change_time or (current_time - key_change_time) / 1000 >= key_change_time_interval:
                # 이미 다른 프로세스가 처리 중인 경우 대기
        while is_processing:
            time.sleep(0.2)  # 0.2초 대기 후 다시 확인

        # 처리 시작
        is_processing = True
        try:
            public_key, private_key = generate_key()  # 키 생성 함수 호출
            key_change_time = current_time

            if key_obj:  # 기존 키가 있으면 갱신
                key_obj.key_timestamp = key_change_time
                key_obj.pub_key = public_key
                key_obj.priv_key = private_key
                db.session.commit()
            else:  # 키가 없으면 새로 저장
                # 새로운 KeyStore 인스턴스 생성
                new_key = KeyStore(
                    pub_key=public_key,
                    priv_key=private_key,
                    key_timestamp=key_change_time
                )
                db.session.add(new_key)  # 세션에 추가
                db.session.commit()  # 커밋
        finally:
            # 처리 종료 후 플래그를 해제해야 다른 요청이 처리 가능
            is_processing = False

    return public_key

def get_private_key():
    key_object = KeyStore.query.first()
    return key_object.priv_key if key_object else None


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  