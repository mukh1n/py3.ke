class FakeApiProxy:
  def get(self, command):
    print('Fake sending: ' + command)
    return 'result=1&login=123&huyPizda=1488'