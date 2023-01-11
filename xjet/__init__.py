
from httpx import AsyncClient
from nacl.signing import SigningKey
import time
import json

from .methods import Account, Cheques, Invoices


class JetAPI(
    Account,
    Cheques,
    Invoices,
):
    def __init__(self, api_key: str, private_key: str = None, host: str = 'https://xjet.app/api/v1'):
        self.api_key = api_key
        self.private_key = bytes.fromhex(private_key) if private_key else None
        self.host = host[:-1] if host.endswith('/') else host

        self.client = AsyncClient(headers={'X-API-Key': self.api_key})
        self.default_timeout = 60

    async def request(self, method, endpoint, **kwargs):
        res = (await self.client.request(
            method, f'{self.host}{endpoint}', **kwargs
        )).json()
        if res.get('error'):
            raise Exception(res['error'])

        return res

    def sign_message(self, message: dict):
        if 'query_id' not in message:
            message['query_id'] = int(time.time() + 60) << 16

        message['signature'] = SigningKey(self.private_key).sign(
            json.dumps(message).encode()
        )._signature.hex()
        return message




