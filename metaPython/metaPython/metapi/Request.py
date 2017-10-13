class Request(object):
  """Request object that takes methon_name and params dictionary and builds command string."""
  def __init__(self, methon_name, params):
    self.methon_name = methon_name
    self.params = params
    if params is not None:
      for key, value in params.items():
        self.params[key] = value
    self.string = 'action={}&'.format(self.methon_name) + '&'.join(['{0}={1}'.format(key, value) for (key, value) in self.params.items() if value is not None and key != 'self'])