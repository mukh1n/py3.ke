class Response(object):
  """Response object that builts from form-data string"""
  def __init__(self, stringResult):
    self.__dict__ = self.parseFormData(stringResult)
    
  def __getattr__(self, name):
    return self.__dict__.get(name)
    
  def parseFormData(self, result):
    dictionary = {}
    keyValueStrings = result.split('&')
    for keyValueString in keyValueStrings:
      keyValue = keyValueString.split('=')
      key = keyValue[0]
      value = keyValue[1]
      dictionary[key] = value
    return dictionary