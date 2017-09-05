class YobaRequest:
  def __init__(self, name, id):
    self.name = name
    self.id = id
  
  @staticmethod
  def createDefault():
    return YobaRequest('defaultName', 666)
    
  def toString(self):
    string = 'name={0}&id={1}'.format(self.name, self.id)
    return string
    
    
request1 = YobaRequest.createDefault();
request2 = YobaRequest('хуй', 1488)

print('request1.name = ' + request1.name)
print('request1.id = ' + str(request1.id))
print('request2.name = ' + request2.name)
print('request2.id = ' + str(request2.id))

print('request1.toString() = ' + request1.toString())
print('request2.toString() = ' + request2.toString())

