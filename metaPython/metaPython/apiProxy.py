import socket

class FakeApiProxy:
  def get(self, command):
    print('Fake sending: ' + command)
    return 'result=1&login=123&huyPizda=1488'

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
