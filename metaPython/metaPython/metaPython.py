from ModifyAccount import ModifyAccountAction

request1 = ModifyAccountAction.createDefault();
request2 = ModifyAccountAction(1234, 'yobaGroup', 200)


print('request1.toString() = ' + request1.toString())
print('request2.toString() = ' + request2.toString())

