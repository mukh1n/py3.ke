import requests
import xml.etree.ElementTree as ET

loginUrl = 'https://web-order.london-demo.lmax.com/auth/login?response_type=code&redirect_uri=https%3A%2F%2Fweb-order.london-demo.lmax.com%2Foauth&client_id=TRADING'
longPollKeyUrl = 'https://web-order.london-demo.lmax.com/secure/longPollKey'
subscribeUrl = 'https://web-order.london-demo.lmax.com/secure/subscribe'
longPollUrl = 'https://web-order.london-demo.lmax.com/push/longPoll'

s = requests.session()

result1 = s.post(loginUrl, data={"username": "yobasha", "password":"yobasha123"})
print('\nLogin: {} {}'.format(result1.status_code , result1.reason))

result2 = s.get(longPollKeyUrl, headers = {"Accept":"application/json"})
longPollKey = result2.json()['res'][0]['body'][0]['longPollKey'][0];
print('\nLong Polling key: ' + longPollKey)

result3 = s.post(subscribeUrl, json={"req":[{"req":[{"subscription":[{"instrument":"4006"}],
                                                     "subscription":[{"orderBookStatus":"4006"}],
                                                     "subscription":[{"exchangeRate":[{"from":"JPY","to":"USD"}]}],
                                                     "subscription":[{"ob2":"4006"}],
                                                     "longPollKey":str(longPollKey)}]}]})

print('\nLong Polling subscribe: ' + result3.json()['res'][0]['header'][0]['status'][0])



for x in range(1,1000):
  res = s.post(longPollUrl, headers={"Accept":"application/json", "longPollKey": longPollKey, "lastReceivedMessageSequence":str(x) })
  root = res.json()['events'][0]
  print('Seq = ' + root['header'][0]['seq'][0])
  body = res.json()['events'][0]['body'][0]
  print(body)
  #exrate = body['exchangeRate'][0]
  #print('{} -> {} = {}'.format(exrate['from'][0], exrate['to'][0], exrate['buy'][0]))