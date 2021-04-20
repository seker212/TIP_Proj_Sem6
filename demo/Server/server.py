import socket
import threading
class Server(object):
    def __init__(self,tcp_port,udp_port) -> None:
        self.ip = socket.gethostbyname(socket.gethostname())
        self.tcp_port = tcp_port
        #self.udp_port = udp_port
        self.running = True

        try:
            self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_sock.bind((self.ip,self.tcp_port))
            #self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #self.udp_sock.bind((self.ip,self.udp_port))

        except:
            print('ERROR: couln\'t bind ports')

        self.connections = []

    def run(self):
        print('TCP running on: ' + str(self.ip) + ':' + str(self.tcp_port))
        #print('UDP running on: ' + str(self.ip) + ':' + str(self.udp_port))

        self.tcp_sock.listen(20)

        while True:
            continue

server = Server(8000,8001)
server.run()