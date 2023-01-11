

class Cheques:
    async def cheque_create(
        self, currency: str, amount: int,
        expires: int = None, description: str = '',
        activates_count: int = 1, groups_id: list = None,
        personal_id: str = None, password: str = None,
        **kwargs
    ):
        query = {
            'currency': currency,
            'amount': amount,
            'expires': expires,
            'description': description,
            'activates_count': activates_count,
            'groups_id': groups_id,
            'personal_id': personal_id,
            'password': password,
            **kwargs
        }
        query = self.sign_message(query)

        return await self.request('POST', '/cheque.create', json=query)

    async def cheque_status(self, cheque_id: int):
        return await self.request('GET', '/cheque.status', params={'cheque_id': cheque_id})

    async def cheque_list(self):
        return await self.request('GET', '/cheque.list')

    async def cheque_cancel(self, cheque_id: int):
        return await self.request('POST', '/cheque.cancel', json={'cheque_id': cheque_id})
