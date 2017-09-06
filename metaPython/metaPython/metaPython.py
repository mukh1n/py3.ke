from apiProxy import *
import actions.createAccount as createAccount
import actions.modifyAccount as modifyAccount

def modifyAccountCall(action):
  api = ApiProxy('127.0.0.1', 49410)
  response = api.get(action.toString())
  return modifyAccount.response(response)

def createAccountCall(action):
  api = ApiProxy('127.0.0.1', 49410)
  response = api.get(action.toString())
  return createAccount.response(response)

action1 = createAccount.action(1234, 'yobaGroup', 200)
result1 = createAccountCall(action1)

print('result1.result = {0}'.format(result1.result))
print('result1.login = {0}'.format(result1.login))
print('result1.error = {0}'.format(result1.error))

action2 = createAccount.action.createDefault()
result2 = createAccountCall(action2)

print('result2.result = {0}'.format(result2.result))
print('result2.login = {0}'.format(result2.login))
print('result2.error = {0}'.format(result2.error))

action3 = modifyAccount.action.createDefault()
result3 = modifyAccountCall(action3)

print('result3.result = {0}'.format(result3.result))
print('result3.login = {0}'.format(result3.login))
print('result3.error = {0}'.format(result3.error))



