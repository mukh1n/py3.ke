class Response(object):
  """Response object that builts from form-data string"""
  def __init__(self, dictionary):
    self.__dict__ = dictionary

  def __getattr__(self, name):
    return self.__dict__.get(name)
    
  @classmethod
  def fromFormData(cls, string):
    d = Response.parseFormData(string)
    return cls(d)

  @classmethod
  def fromScsv(cls, string, headers):
    d = Response.parseFromScsv(string, headers)
    return cls(d)

  def parseFormData(result):
    dictionary = {}
    keyValueStrings = result.split('&')
    for keyValueString in keyValueStrings:
      keyValue = keyValueString.split('=')
      key = keyValue[0]
      value = keyValue[1]
      dictionary[key] = value
    return dictionary

  def parseFromScsv(scsv, headers):
    rows = scsv.split('\n')
    dictionary = Response.parseFormData(rows[0])
    headersList = list(map(str.strip, headers.split(';')))
    items = []
    for i in range(1, len(rows) - 1):
        row = rows[i]
        itemDict = {}
        values = row.split(';')
        for x in range(0, len(headersList) - 1):
          itemDict[headersList[x]] = values[x]
        items.append(Response(dictionary = itemDict))
    dictionary['items'] = items;
    return dictionary