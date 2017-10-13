from metapi import *
from apiProxy import *

proxy = FakeApiProxy()
client = ApiClient(proxy)

#accountResult = client.createAccount(name='123',group='1234',password='123123445', comment = 'uoba')
getOrderResult = client.getOrder('sooqa')

print(getOrderResult.open_price)
print(getOrderResult.close_time)