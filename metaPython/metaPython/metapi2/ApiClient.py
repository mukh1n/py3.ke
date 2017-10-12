import metapi2

class ApiClient(object):
    """description of class"""
    def __init__(self, apiProxy):
      self.apiProxy = apiProxy
  
    def createAccount(self, **kwargs):
      result = metapi2.Request(methon_name = 'create_account', 
                        allowed_args =  ['name', 'group', 'password', 'comment', 'huy', 'leverage'],
                        required_args = ['name', 'group', 'password'])(self.apiProxy, **kwargs)
      return metapi2.Response(result)