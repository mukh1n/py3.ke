class Response(object):
  """Response object that builts from form-data string"""
  def __init__(self, string, headers):
    if headers is None:
      self.__dict__ = self.parseFormData(string)
    else:
      self.__dict__ = self.parseFromScsv(string, headers)
    
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

  def parseFromScsv(self, scsv, headers):
    dictionary = {}
    headersList = [header.strip() for header in headers.split(';')]
    valueList = [value for value in scsv.split(';')]
    for i in range(0, len(headersList)-1):
      dictionary[headersList[i]] = valueList[i]
    return dictionary