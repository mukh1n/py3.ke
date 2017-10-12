class Request(object):
    """description of class"""
    def __init__(self, methon_name, allowed_args, required_args):
      self.methon_name = methon_name
      self.allowed_args = allowed_args
      self.required_args = required_args
      self.params = {}
    
    def __call__(self, apiProxy, **kwargs):
      if kwargs is not None:
        for key, value in kwargs.items():
          if key not in self.allowed_args:
            raise ValueError('Oops, argument "{}" not allowed for method "{}"'.format(key, self.methon_name))
          else:
            self.params[key] = value
      for key in self.required_args:
        if key not in self.params.keys():
          raise ValueError('Oops, argument "{}" is required for method "{}"'.format(key, self.methon_name))
      return apiProxy.get(self.string)
    
    @property
    def string(self):
      return 'action={}&'.format(self.methon_name) + '&'.join(['{0}={1}'.format(key, value) for (key, value) in self.params.items() if value is not None and key != 'self'])