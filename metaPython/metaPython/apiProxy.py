import socket

class FakeApiProxy:
  def get(self, command):
    print('Fake sending: ' + command)
    #return 'result=1&login=123&huyPizda=1488'
    return '102;3871341;EURUSD;1.18427;1.18424;-3.00;100;1507913188;0;-781901231-177781462-1563176667;0.00;0.00;0;0.00000;0.00000;0.00'

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
