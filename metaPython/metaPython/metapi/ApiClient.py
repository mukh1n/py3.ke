import metapi

class ApiClient(object):
  """Api Client for Meta Trader 5 API"""
  def __init__(self, apiProxy):
    self.apiProxy = apiProxy

  def do(self, method_name, params, headers=None):
    request = metapi.Request(method_name, params)
    result = self.apiProxy.get(request.string)
    if headers is None:
      return metapi.Response.fromFormData(result)
    else:
      return metapi.Response.fromScsv(result, headers)

  def createAccount(self, name, group, password, login=None, agent=None, leverage=None, email=None, id=None, address=None,
                   city=None, state=None, zipcode=None, country=None, phone=None, password_phone=None, password_investor=None, 
                   comment=None, enable=None, enable_change_password=None, enable_read_only=None, send_reports=None, status=None):
    return self.do('createaccount', locals())

  def createGroup(self, name, currency=None, company=None, smtp_server=None, smtp_login=None, smtp_password=None, smtp_email=None,
                default_leverage=None, default_deposit=None, copies=None, reports=None, margin_call=None, margin_mode=None, margin_stopout=None,
                news=None, interestrate=None, use_swap=None, hedge_prohibited=None, margin_type=None, enable=None, request_id=None,):
    return self.do('creategroup', locals())

  def getOrder(self, order, request_id=None):
    return self.do('getorder', locals(), 'login; order; symbol; open_price; close_price; profit; volume; open_time; close_time; comment; commission; agent; cmd; sl; tp; swap')

  def getSymbol(self, request_id=None):
    return self.do('getsymbol', locals(), 'symbol_name; digits; security; security_type; swapLong; swapShort; spread; bid; ask; tickSize; tickPrice; initial_margin; contract_size; point')