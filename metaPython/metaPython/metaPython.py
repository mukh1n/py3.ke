from modifyAccount import *

request1 = ModifyAccountAction.createDefault();
request2 = ModifyAccountAction(1234, 'yobaGroup', 200)

printer(request1)
print('request1.toString() = ' + request1.toString())
print('request2.toString() = ' + request2.toString())



def printer(action):
    print(action.toString())