class ModifyAccountAction:
  def __init__(self, login, group, leverage):
    self.commandName = 'modifyaccount'
    self.login = login
    self.group = group
    self.leverage = leverage
  
  @staticmethod
  def createDefault():
    return ModifyAccountAction('defaultLogin', 'defaultGroup', 200)
    
  def toString(self):
    string = 'action={0}&login={1}&group={2}&leverage={3}'.format(self.commandName, self.login, self.group, self.leverage)
    return string
