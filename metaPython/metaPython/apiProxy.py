import socket

class FakeApiProxy:
  def __init__(self):
    self.c = 0

  def get(self, command):
    print('Fake sending: ' + command)
    self.c = self.c+1
    return 'result=1&login=123&huyPizda=1488' if self.c == 1 else """result=1&symbolsCount=853&size=79232
EURGBP;5;0;Forex;-3.97500;0.33500;0;0.89123;0.89126;0.00000;0.00000;0.00000;100000.000000;0.00001
GBPUSD;5;0;Forex;-9.15000;1.02500;0;1.04027;1.04030;0.00000;0.00000;0.00000;100000.000000;0.00001
EURUSD;5;0;Forex;-10.26000;2.42000;0;1.18426;1.18427;0.00001;0.10000;100000.00000;100000.000000;0.00001
USDJPY;3;0;Forex;1.08000;-9.30000;0;110.48700;110.49100;0.00000;0.00000;0.00000;100000.000000;0.001
NZDUSD;5;0;Forex;0.19500;-3.58500;0;0.72160;0.72166;0.00000;0.00000;0.00000;100000.000000;0.00001"""

class ApiProxy:
  def __init__(self, host, port):
    self.host = host
    self.port = port
    
  def get(self, command):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((self.host, self.port))
    num = mySocket.send(command)
    result = self.recv_msg(mySocket)
    mySocket.close()
    return result
    
  def recv_msg(self, sock):
    messageLength = self.recv_lenght(sock)
    if not messageLength:
        return None
    return self.recv_all(sock, messageLength)
    
  def recv_lenght(self, sock):
    packet = sock.recv(100)
    if not packet:
        return None
    len = packet.rstrip()
    return int(len)

  def recv_all(self, sock, n):
    data = ''
    while len(data) < n:
      packet = sock.recv(n - len(data))
      if not packet:
        return data
      data += str(packet).decode('utf-8')
    return data
