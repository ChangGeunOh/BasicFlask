
import base64
from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from flask import request

keyChangeTime = None
key_change_time_interval = 3600
public_key, private_key = None, None


# RSA 키 Pair(public, private) 생성 함수
def generate_key():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.public_key().export_key()
    return public_key.decode("utf-8"), private_key.decode("utf-8")

# RSA 암호화 함수
def rsa_encrypt(pubkey, raw):
    cipher_rsa = PKCS1_v1_5.new(RSA.import_key(pubkey))
    encrypted = cipher_rsa.encrypt(raw.encode("utf-8"))
    b64_encrypted = base64.b64encode(encrypted).decode('utf-8')
    return b64_encrypted

# RSA 복호화 함수
def rsa_decrypt(privkey, encrypted):
    cipher_rsa = PKCS1_v1_5.new(RSA.import_key(privkey))
    encrypted_data = encrypted.encode("utf-8")
    base64_data = base64.b64decode(encrypted_data)
    data = cipher_rsa.decrypt(base64_data, None)
    raw = data.decode('utf-8')
    return raw

# 클라이언트 IP 가져오기 함수
def get_client_ip():
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    else:
        ip = request.remote_addr
    return ip