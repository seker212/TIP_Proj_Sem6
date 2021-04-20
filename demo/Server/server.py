import socket
import threading

class Connection(object):
    def __init__(self,conn,address) -> None:
        self.conn = conn
        self.address = address

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

        while self.running:
            try:
                connection = Connection(self.tcp_sock.accept())
                self.connections.append(connection)
                threading.Thread(target=self.streamAudio,args=(connection)).start()

            except Exception as err:
                print(str(err))
                pass
        
    def streamAudio(self,connection):
        while self.running and (connection in self.connections):
            try:
                data = connection.conn.recv(1024)
                for other_connection in self.connections:
                    if other_connection != connection:
                        other_connection.conn.send(data)
            except:
                connection.conn.close()
                self.connections.remove(connection)


server = Server(8000,8001)
server.run()