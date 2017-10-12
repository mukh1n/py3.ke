class Response:
  _getattr_ = dict.__getitem__
  def __init__(self, stringResult):
    self.__dict__ = self.parseResult(stringResult)
    
  def parseResult(self, result):
    dictionary = {}
    keyValueStrings = result.split('&')
    for keyValueString in keyValueStrings:
      keyValue = keyValueString.split('=')
      key = keyValue[0]
      value = keyValue[1]
      dictionary[key] = value
    return dictionary

class Request:
  def __init__(self, methon_name, allowed_args):
    self.methon_name = methon_name
    self.allowed_args = allowed_args
    self.params = {}
    
  def __call__(self, **kwargs):
    if kwargs is not None:
      for key, value in kwargs.items():
        if key not in self.allowed_args:
          raise ValueError('Oops, argument {} not allowed for method {}'.format(key, self.methon_name))
        else:
          self.params[key] = value
    return self.string
    
  @property
  def string(self):
    return 'action='+self.methon_name +'&'+'&'.join(['{0}={1}'.format(key, value) for (key, value) in self.params.items() if value is not None and key != 'self'])
    
class Api:
  def createAccount(self, **kwargs):
    result = Request(methon_name = 'create_account', allowed_args = ['login', 'name', 'huy'])(**kwargs)
    return Response(result)

api = Api()
result1 = api.createAccount(login=1234, name='yoba')
result2 = api.createAccount(login=1234, name='yoba', huy='wat')
#result = api.createAccount(login=1234, name='yoba', pizda='wat').print() #ошибка

result1

response = Response('huy=pizda&vodka=zbs')

print(response.huy)
print(response.vodka)