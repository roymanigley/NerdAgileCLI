from base64 import b64decode, b64encode
from hashlib import sha512
from json import loads, dumps

from django.contrib.auth.models import User
from ninja.security import HttpBearer


class AuthBearer(HttpBearer):
    def authenticate(self, request, token) -> str:
        token_dict = token_to_dict(token)
        username = token_dict['username']
        check_sum = token_dict['check_sum']
        user_hash = __generate_token_checksum__(username)
        if user_hash == check_sum:
            return token


class TokenIssuer(object):

    @staticmethod
    def issue_token(username: str, password: str) -> dict or None:
        user: User = User.objects.get_by_natural_key(username)
        is_api_user = user.groups.filter(name='API_USER').exists()
        if user is not None and is_api_user and user.check_password(password):
            check_sum = __generate_token_checksum__(username)
            dumps({"username": username, "check_sum": check_sum})
            token = b64encode(f'{{ "username": "{username}", "check_sum": "{check_sum}" }}'.encode('utf-8')).decode('utf-8')
            return {"token": token}
        return None


def __generate_token_checksum__(username: str) -> str:
    return sha512(username.encode('utf-8')).hexdigest()


def token_to_dict(token: str) -> dict:
    token_decoded = b64decode(token.encode('utf-8')).decode('utf-8')
    return loads(token_decoded)
