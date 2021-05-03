import socket
import threading

class Connection(object):
    def __init__(self,conn,address, nick) -> None:
        self.conn = conn
        self.address = address
        self.nick = nick

class Server(object):
    def __init__(self,tcp_port,udp_port) -> None:
        self.ip = "127.0.0.1" # socket.gethostbyname(socket.gethostname())
        self.tcp_port = tcp_port
        #self.udp_port = udp_port
        self.running = True

        try:
            self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_sock.bind((self.ip,self.tcp_port))
            #self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #self.udp_sock.bind((self.ip,self.udp_port))

        except Exception as err:
            print('ERROR: couln\'t bind ports')
            print('err')
            sys.exit(1)

        self.connections = []

    def run(self):
        print('TCP running on: ' + str(self.ip) + ':' + str(self.tcp_port))
        #print('UDP running on: ' + str(self.ip) + ':' + str(self.udp_port))

        self.tcp_sock.listen(20)

        while self.running:
            try:
                conn, address = self.tcp_sock.accept()
                nick = conn.recv(1024)
                nick = str(nick, 'UTF-16')
                if(self.validate_nick(nick)):
                    conn.send(bytes("ack",'UTF-8'))
                    connection = Connection(conn, address, nick)
                    self.connections.append(connection)
                    threading.Thread(target=self.streamAudio,args=[connection]).start()
                else:
                    conn.send(bytes("nak",'UTF-8'))
                    conn.close()

            except Exception as err:
                print(str(err))
                pass
        
    def streamAudio(self,connection):
        while self.running and (connection in self.connections):
            try:
                data = connection.conn.recv(1024*4)
                for other_connection in self.connections:
                    if other_connection != connection:
                        other_connection.conn.send(data)
            except:
                connection.conn.close()
                self.connections.remove(connection)
    
    def validate_nick(self,nick):
        for con in self.connections:
            if con.nick == nick:
                return False
        return True


server = Server(8000,8001)
server.run()