class Request:
  def __init__(self, methon_name, allowed_args, required_args):
    self.methon_name = methon_name
    self.allowed_args = allowed_args
    self.required_args = required_args
    self.params = {}
    
  def __call__(self, apiProxy, **kwargs):
    if kwargs is not None:
      for key, value in kwargs.items():
        if key not in self.allowed_args:
          raise ValueError('Oops, argument "{}" not allowed for method "{}"'.format(key, self.methon_name))
        else:
          self.params[key] = value
    for key in self.required_args:
      if key not in self.params.keys():
        raise ValueError('Oops, argument "{}" is required for method "{}"'.format(key, self.methon_name))
    return apiProxy.get(self.string)
    
  @property
  def string(self):
    return 'action={}&'.format(self.methon_name) + '&'.join(['{0}={1}'.format(key, value) for (key, value) in self.params.items() if value is not None and key != 'self'])

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

class Api:
  def __init__(self, apiProxy):
    self.apiProxy = apiProxy
  
  def createAccount(self, **kwargs):
    result = Request(methon_name = 'create_account', 
                      allowed_args =  ['name', 'group', 'password', 'comment', 'huy', 'leverage'],
                      required_args = ['name', 'group', 'password'])(self.apiProxy, **kwargs)
    return Response(result)

