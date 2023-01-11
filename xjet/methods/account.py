

class Account:
    async def me(self):
        return await self.request('GET', '/account.me')

    async def balances(self):
        return await self.request('GET', '/account.balances')

    async def submit_deposit(self):
        return await self.request('POST', '/account.submitDeposit')

    async def withdraw(self, ton_address: str, currency: str, amount: float):
        query = {
            'ton_address': ton_address,
            'currency': currency,
            'amount': amount
        }
        query = self.sign_message(query)

        return await self.request('POST', '/account.withdraw', json=query)
