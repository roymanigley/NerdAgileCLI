import os
from base64 import b64decode, b64encode
from json import loads, dumps

from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from django.contrib.auth.models import User
from ninja.security import HttpBearer

rsa_private_key_path = os.environ.get('RSA_PRIVATE_KEY') or 'rsa_private.pem'
rsa_public_key_path = os.environ.get('RSA_PUBLIC_KEY') or 'rsa_public.pem'

with open(rsa_private_key_path) as f:
    private_key = RSA.importKey(f.read())
    print(private_key)

with open(rsa_public_key_path) as f:
    public_key = RSA.importKey(f.read())
    print(public_key)


class AuthBearer(HttpBearer):
    def authenticate(self, request, token: str) -> str | None:
        if verify_token(token):
            return token
        else:
            print(f'invalid token: {token}')
            return None


class TokenIssuer(object):

    @staticmethod
    def issue_token(username: str, password: str) -> dict or None:
        user: User = User.objects.get_by_natural_key(username)
        is_api_user = user.groups.filter(name='API_USER').exists()
        if user is not None and is_api_user and user.check_password(password):
            token_clear = dumps({"username": username})
            token = b64encode(token_clear.encode('utf-8')).decode('utf-8')
            token = sign_token(token)
            return {"token": token}
        return None


def token_to_dict(token: str) -> dict:
    token = token.split('.')[0]
    token_decoded = b64decode(token.encode('utf-8')).decode('utf-8')
    return loads(token_decoded)


def sign_token(token: str):
    signer = PKCS1_v1_5.new(private_key)
    hash = SHA512.new(token.encode('utf-8'))
    hash.digest()
    sign = signer.sign(hash)
    return f'{token}.{sign.hex()}'

def verify_token(token: str):
    message, signature = token.split('.')
    hash = SHA512.new(message.encode('utf-8'))
    hash.digest()
    verifier = PKCS1_v1_5.new(public_key)
    return verifier.verify(hash, bytes.fromhex(signature))
