import strToDict

class action:
  def __init__(self, login, group, leverage):
    self.commandName = 'modifyaccount'
    self.login = login
    self.group = group
    self.leverage = leverage
  
  @staticmethod
  def createDefault():
    return action('defaultLogin', 'defaultGroup', 200)
    
  def toString(self):
    string = 'action={0}&login={1}&group={2}&leverage={3}'.format(self.commandName, self.login, self.group, self.leverage)
    return string


class response:
  def __init__(self, responseString):
    dict = strToDict.getDict(responseString)
    self.result = dict.get("result")
    self.error = dict.get("error")
    self.login = dict.get("login")