import requests, time

yoba = ["EURUSD"]
r = requests.post('https://requestb.in/zgdlgczg',  json={
                                                          "SlaveLogin": "login",
                                                          "MasterLogin": "master_login",
                                                          "CopySymbols": yoba,
                                                          "CopyMode": "copy_mode",
                                                          "Value": "value"})
print(r.request)
print(str(r.content))
