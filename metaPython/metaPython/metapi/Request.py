class Request(object):
    """description of class"""
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