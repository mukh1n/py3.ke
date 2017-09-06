import strToDict

class action:
  def __init__(self, name, group, leverage, login=''):
    self.commandName = 'createaccount'
    self.name = name
    self.login = login
    self.group = group
    self.leverage = leverage

  @staticmethod
  def createDefault():
    return action('defaultName', 'defaultGroup', 200)
  
  def toString(self):
    return 'action=createaccount&name={0}&group={1}&leverage={2}&enable_read_only=0&login={3}\\0'.format(self.name, self.group, self.leverage, self.login)
    

class response:
  def __init__(self, responseString):
    dict = strToDict.getDict(responseString)
    self.result = dict.get("result")
    self.error = dict.get("error")
    self.login = dict.get("login")