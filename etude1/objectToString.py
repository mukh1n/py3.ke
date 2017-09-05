def parseString(result):
  dictionary = {}
  keyValueStrings = result.split('&')
  for keyValueString in keyValueStrings:
    keyValue = keyValueString.split('=')
    key = keyValue[0]
    value = keyValue[1]
    dictionary[key] = value
  return dictionary


class YobaResponse:
  def __init__(self, string):
    dictionary = parseString(string)
    self.users = dictionary.get('users')
    self.answer = dictionary.get('answer')
    self.requestId = dictionary.get('request_id')
    self.result = dictionary.get('result')
    
  
def getSomeResponseFromServer():
  return 'users=1&answer=1700;55939%0a&request_id=1488&result=1'
  
  
someResponseString = getSomeResponseFromServer()
response = YobaResponse(someResponseString)


#теперь можна работать с респонсом по человечески, как с объектом
print('response.users = ' + response.users)
print('response.answer = ' + response.answer)
print('response.requestId = ' + str(response.requestId))
print('response.result = ' + str(response.result))