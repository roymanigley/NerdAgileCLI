import json
from typing import List, Generic, TypeVar
from urllib import parse
from urllib.request import Request, urlopen

from model import ClassMapper

T = TypeVar('T')


class GenericClient(Generic[T]):

    def __init__(self, base_url: str, resource_path: str, username: str, password: str):
        self.base_url: str = base_url
        self.resource_url: str = resource_path
        self.username = username
        self.password = password

    def get_token(self, username, password) -> str:
        params = parse.urlencode({'username': username, 'password': password})
        req = Request(
            f'{self.base_url}/api/login?{params}',
            method='POST',
        )
        json_bytes: bytes = urlopen(req).read()
        return json.loads(json_bytes)['token']


    def find_all(self) -> List[T]:
        token = self.get_token(self.username, self.password)
        req = Request(
            f'{self.base_url}{self.resource_url}',
            method='GET',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}'
            }
        )
        json_bytes: bytes = urlopen(req).read()
        records: List = json.loads(json_bytes)
        return list(map(lambda record: ClassMapper(record).to_class(), records))

    def find_one(self, id: int) -> T:
        token = self.get_token(self.username, self.password)
        req = Request(
            f'{self.base_url}{self.resource_url}/{id}',
            method='GET',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}'
            }
        )
        json_bytes: bytes = urlopen(req).read()
        record: List = json.loads(json_bytes)
        return ClassMapper(record).to_class()

    def create(self, payload: T) -> T:
        token = self.get_token(self.username, self.password)
        json_string: str = json.dumps(payload.__dict__)
        print(json_string)
        req = Request(
            f'{self.base_url}{self.resource_url}',
            method='POST',
            data=json_string.encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}'
            }
        )
        json_bytes: bytes = urlopen(req).read()
        record: List = json.loads(json_bytes)
        return ClassMapper(record).to_class()

    def update(self, payload: T, id: int) -> T:
        token = self.get_token(self.username, self.password)
        json_string: str = json.dumps(payload.__dict__)
        req = Request(
            f'{self.base_url}{self.resource_url}/{id}',
            method='PUT',
            data=json_string.encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}'
            }
        )
        json_bytes: bytes = urlopen(req).read()
        record: List = json.loads(json_bytes)
        return ClassMapper(record).to_class()

    def delete(self, id: int):
        token = self.get_token(self.username, self.password)
        req = Request(
            f'{self.base_url}{self.resource_url}/{id}',
            method='DELETE',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}'
            }
        )
        urlopen(req).read()
