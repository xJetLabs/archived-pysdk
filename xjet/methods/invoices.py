

class Invoices:
    async def invoice_create(
        self, currency: str, amount: int,
        description: str = None, max_payments: int = 1
    ):
        return await self.request(
            'POST', '/invoice.create', json={
                'currency': currency,
                'amount': amount,
                'description': description,
                'max_payments': max_payments
            }
        )

    async def invoice_status(self, invoice_id: int):
        return await self.request('GET', '/invoice.status', params={'invoice_id': invoice_id})

    async def invoice_list(self):
        return await self.request('GET', '/invoice.list')

