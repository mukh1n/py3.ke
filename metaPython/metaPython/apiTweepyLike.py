class API(object):
  @property
  def create_account(self):
    return APIMethod(api=self,
        action_name='create_account',
        allowed_param=['login_id', 'leverage', 'balance'])

class APIMethod(object):
  def __init__(self, api, args, kwargs):
    self.api = api
    self.action_name = config.get('action_name', None)
    self.allowed_param = config.get('allowed_param', [])
    self.build_parameters(args, kwargs)
            
  def build_parameters(self, args, kwargs):
    self.params = {}
    for idx, arg in enumerate(args):
      if arg is None:
        continue
      try:
        self.params[self.allowed_param[idx]] = convert_to_utf8_str(arg)
      except IndexError:
        raise TweepError('Too many parameters supplied!')
    for k, arg in kwargs.items():
      if arg is None:
        continue
      if k in self.params:
        raise TweepError('Multiple values for parameter %s supplied!' % k)
      self.params[k] = arg

  def execute(self):
      url = 'action={}&'.format(self.action_name) + '&'.join(['{0}={1}'.format(key, value) for (key, value) in self.params.items() if value is not None and key != 'self'])
      print(url)

def _call(*args, **kwargs):
    method = APIMethod(args, kwargs)
    if kwargs.get('create'):
        return method
    else:
        return method.execute()




api = API()
public_tweets = api.create_account(login_id=123)