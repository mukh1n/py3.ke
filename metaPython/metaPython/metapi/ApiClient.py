import metapi

class ApiClient(object):
    """description of class"""
    def __init__(self, apiProxy):
      self.apiProxy = apiProxy

    def createAccount(self, name, group, password
          , login=None, agent=None, leverage=None, email=None, id=None, address=None, city=None, state=None
          , zipcode=None, country=None, phone=None, password_phone=None, password_investor=None
          , comment=None, enable=None, enable_change_password=None
          , enable_read_only=None, send_reports=None, status=None):
      result = metapi.Request(methon_name = 'create_account')(self.apiProxy, locals())
      return metapi.Response(result)
