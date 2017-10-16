import time
import socket
import threading

class Pumper:
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.isPumping = False
    
  def start(self, command):
    print ('[{0}] Start pumping: {1}'.format(threading.currentThread().getName(), command))
    if self.isPumping:
      return
    self.isPumping = True
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((self.host, self.port))
    self.socket.send(command.encode())
    received = True
    while received and self.isPumping:
      received = self.socket.recv(1024).decode("utf-8")
      print('[{0}] Recieved updates: {1}'.format(threading.currentThread().getName(), received))
    self.socket.close()
    print('[{0}] Pumping stoped.'.format(threading.currentThread().getName()))
    
  def stop(self):
    if not self.isPumping:
      return
    self.isPumping = False


pumpers = []

#создаём 5 памперов
for i in range(5):
  pumper = Pumper('127.0.0.1', 49410)
  pumpers.append(pumper)
  
#для каждого пампера создаём поток и вызываем pumper.start('action=pumping&equity=1\0')
for pumper in pumpers:
  newThread = threading.Thread(target=pumper.start, args=('action=pumping&equity=1\0',))
  newThread.start()
  
#ждём пока пользователь консоли нажмёт Enter
input("Press Enter to stop...")

#останавливаем всех памперов
for pumper in pumpers:
  pumper.stop()

