import datetime
from datetime import datetime

from nerd_agile_cli_rest_api.rest.auth import token_to_dict


def apply_autit_create_infos(payload, request):
    payload_dict = payload.dict()
    token = request.headers.get('Authorization')[7:].split('.')[0]
    username = token_to_dict(token)['username']
    payload_dict['creator'] = username
    payload_dict['create_date'] = datetime.utcnow()
    return payload_dict
