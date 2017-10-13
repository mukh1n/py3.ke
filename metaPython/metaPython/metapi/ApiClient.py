import metapi

class ApiClient(object):
  """description of class"""
  def __init__(self, apiProxy):
    self.apiProxy = apiProxy

  def do(self, request):
    result = self.apiProxy.get(request.string)
    return metapi.Response(result)

  def createAccount(self, name, group, password
        , login=None, agent=None, leverage=None, email=None, id=None, address=None, city=None, state=None
        , zipcode=None, country=None, phone=None, password_phone=None, password_investor=None
        , comment=None, enable=None, enable_change_password=None
        , enable_read_only=None, send_reports=None, status=None):
    request = metapi.Request(methon_name = 'create_account', params = locals())
    return self.do(request)
