class Response:
  def __init__(self, stringResult):
    self.__dict__ = self.parseResult(stringResult)
    
  def __getattr__(self, name):
    return self.__dict__.get(name)
    
  def parseResult(self, result):
    dictionary = {}
    keyValueStrings = result.split('&')
    for keyValueString in keyValueStrings:
      keyValue = keyValueString.split('=')
      key = keyValue[0]
      value = keyValue[1]
      dictionary[key] = value
    return dictionary

class FakeApiProxy:
  def get(self, command):
    print('Fake sending: ' + command)
    return 'result=1&login=123&huyPizda=1488'