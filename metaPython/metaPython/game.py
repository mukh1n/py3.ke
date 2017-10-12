import threading
import time
import os
import msvcrt

class Device:
  def __init__(self, name, baseIncome, level):
    self.name = name
    self.baseIncome = baseIncome
    self.level = level
  
  def getIncome(self):
    return self.baseIncome + self.baseIncome * 0.15 * self.level

  def getUpgradeCost(self):
    return self.getIncome() * 10
    
money = 0
devices = {}
devices["1"] = Device('Yoba', 100, 1)
devices["2"] = Device('MaliyYoba', 30, 1)

def getTotalIncome():
  global devices
  result = 0
  for k, device in devices.items():
    result += device.getIncome()
  return result

def iterate():
  global money
  money+=getTotalIncome()
  updateUI()

def start():
  iterate()
  threading.Timer(1, start,).start()

def updateUI():
  global devices
  os.system('cls')
  print('Money: {0}'.format(money))
  print('Income: {0}'.format(getTotalIncome()))
  print('\n\n')
  print('Devices: ')
  for k, d in devices.items():
    print('\t[{0}] {1}. Lvl: {2}. Income: {3}. Money to upgrade: {4}.'.format(k, d.name, d.level, d.getIncome(), d.getUpgradeCost()))
    
start()
while True:
  pressedKey = msvcrt.getch().decode('utf-8') #читаем нажатую клавишу
  device = devices[pressedKey]
  if money < device.getUpgradeCost(): #если денег нет, то нихуя не делаем
    continue
  else:
    money -= device.getUpgradeCost()
    device.level += 1
  updateUI()