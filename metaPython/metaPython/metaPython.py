from metapi import *
from apiProxy import *

proxy = FakeApiProxy()
client = ApiClient(proxy)

accountResult = client.createAccount(name='123',group='1234',password='123123445', comment = 'uoba')
getSymbolResult = client.getSymbol()

print(accountResult.result)
print(accountResult.login)


print(getSymbolResult.result)
print(getSymbolResult.symbolsCount)
print(getSymbolResult.size)
for item in getSymbolResult.items:
  print('got {} / {} / {} / {}'.format(item.symbol_name, item.spread, item.bid, item.ask))