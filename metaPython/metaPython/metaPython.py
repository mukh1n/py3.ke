from metapi import *
from apiProxy import *

proxy = FakeApiProxy()
client = ApiClient(proxy)

accountResult = client.createAccount(name='123',group='1234',password='123123445', comment = 'uoba')
print(accountResult.result)
print(accountResult.login)