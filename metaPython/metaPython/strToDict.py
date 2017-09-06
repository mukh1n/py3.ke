def getDict(string):
  dictionary = {}
  keyValueStrings = string.split('&')
  for keyValueString in keyValueStrings:
    keyValue = keyValueString.split('=')
    key = keyValue[0]
    value = keyValue[1]
    dictionary[key] = value
  return dictionary
