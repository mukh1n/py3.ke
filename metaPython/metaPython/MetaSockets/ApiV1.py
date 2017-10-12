from Common import Response

class Request:
    def __init__(self, methon_name):
      self.methon_name = methon_name
      self.params = {}
    
    def __call__(self, apiProxy, params):
      if params is not None:
        for key, value in params.items():
          self.params[key] = value
      return apiProxy.get(self.string)

    @property
    def string(self):
      return 'action={}&'.format(self.methon_name) + '&'.join(['{0}={1}'.format(key, value) for (key, value) in self.params.items() if value is not None and key != 'self'])

class Api:  
  def __init__(self, apiProxy):
    self.apiProxy = apiProxy

  def createAccount(self, name, group, password
        , login=None, agent=None, leverage=None, email=None, id=None, address=None, city=None, state=None
        , zipcode=None, country=None, phone=None, password_phone=None, password_investor=None
        , comment=None, enable=None, enable_change_password=None
        , enable_read_only=None, send_reports=None, status=None):
    result = Request(methon_name = 'create_account')(self.apiProxy, locals())
    return Response(result)
