import strToDict

class Response:
  def __init__(self, responseString):
    dict = strToDict.getDict(responseString)
    self.p = dict
    self.result = dict.get("result")
    self.error = dict.get("error")
    self.login = dict.get("login")
    self.size = dict.get("size")
    self.request_id = dict.get("request_id")

class Command:
  def __init__(self, name, params):
    self.name = name
    self.params = params
  
  def toString(self):
    return 'action=' + self.name + '&'.join(['{0}={1}'.format(key, value) for (key, value) in self.params.items() if value is not None and key != 'self'])

  def do(self):
    api = ApiProxy()
    result = api.send(self)
    return Response(result)

class CommandBuilder:
  def create_account(self, name, group, password
          , login=None, agent=None, leverage=None, email=None, id=None, address=None, city=None, state=None
          , zipcode=None, country=None, phone=None, password_phone=None, password_investor=None
          , comment=None, enable=None, enable_change_password=None
          , enable_read_only=None, send_reports=None, status=None):
    return Command('createaccount', locals())

  def modify_account(self, login, name2, group, password
          , agent=None, leverage=None, email=None, id=None, address=None, city=None, state=None
          , zipcode=None, country=None, phone=None, password_phone=None, password_investor=None
          , comment=None, enable=None, enable_change_password=None
          , enable_read_only=None, send_reports=None, status=None):
    return Command('modifyaccount', locals())

class ApiProxy:
  def send(self, command):
    print('Кабудто шлём: [{0}] - {1}'.format(command.name, command.toString()))
    return 'result=1&login=123&huyPizda=1488'

a = ApiProxy()
b = CommandBuilder()
result1 = b.create_account('123','444','2355', phone=1488).do()
result2 = b.create_account('90000', '123','444','2355', phone=666).do()
print(result1.request_id)
print(result1.result)
print(result1.p["huyPizda"])
print(result2.request_id)
print(result2.result)
print(result2.p["huyPizda"])