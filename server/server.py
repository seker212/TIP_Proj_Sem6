#TODO cleanup?

import socket
import sys
import threading
import time
from os import getenv

class Connection(object):
    def __init__(self, conn, address, nick, udp_port) -> None:
        self.conn = conn
        self.address = address
        self.nick: str = nick
        self.udp_port: int = udp_port
    
    def __repr__(self) -> str:
        return f'<Connetcion: {self.conn}; addr TCP: {self.address}; nick: {self.nick}; udp port: {self.udp_port}>'

class Server(object):
    def __init__(self,tcp_port,udp_port, ip) -> None:
        self.ip = ip # TODO: socket.gethostbyname(socket.gethostname())
        self.tcp_port = tcp_port
        self.udp_port = udp_port
        self.running = True
        self.max_participants = 10

        try:
            self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_sock.bind((self.ip,self.tcp_port))
            self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_sock.bind((self.ip,self.udp_port))

        except Exception as err:
            print('ERROR: couln\'t bind ports')
            print(err)
            sys.exit(1)

        self.connections = []

    def run(self):
        print('TCP running on: ' + str(self.ip) + ':' + str(self.tcp_port))

        #TODO UDP
        print('UDP running on: ' + str(self.ip) + ':' + str(self.udp_port))

        self.tcp_sock.listen(20)

        threading.Thread(target=self.streamAudio, daemon=True).start()
        threading.Thread(target=self.ping_tcp, daemon=True).start()
        while self.running:
            try:
                conn, address = self.tcp_sock.accept()
                startinfo = conn.recv(1024)
                startinfo = str(startinfo, 'UTF-16').split(":")
                nick = startinfo[0]
                if (len(self.connections) >= self.max_participants):
                    conn.send(bytes("ful",'UTF-16'))
                    conn.close()
                elif(len(startinfo) == 2 and self.validate_nick(nick) and startinfo[1].isdigit()):
                    connection = Connection(conn, address, nick, int(startinfo[1]))
                    conn.send(bytes(f"ack:{self.udp_port}",'UTF-16'))
                    self.connections.append(connection)
                    print(connection)
                    self.update_nicks()
                else:
                    conn.send(bytes("nak",'UTF-16'))
                    conn.close()

            except Exception as err:
                print(str(err))
                pass
    
    def streamAudio(self):
        while self.running:
            try:
                data, addr = self.udp_sock.recvfrom(4096)
                if self._is_in_connections(addr):
                    for client in self.connections:
                        if client.address[0] != addr[0] or client.udp_port != addr[1]:
                            self.udp_sock.sendto(data, (client.address[0], client.udp_port))

            except Exception as err:
                print(err)
                sys.exit(1)

    def validate_nick(self,nick):
        for con in self.connections:
            if (con.nick == nick or nick == " " or nick == ""):
                return False
        return True

    def update_nicks(self):
        time.sleep(0.2)
        for any_connection in self.connections:
            any_connection.conn.send(bytes("new",'UTF-16'))
        time.sleep(0.001)
        
        for n in self.connections:
            for any_connection in self.connections:
                any_connection.conn.send(bytes(n.nick,'UTF-16'))
            time.sleep(0.001)

        for any_connection in self.connections:
            any_connection.conn.send(bytes("fin",'UTF-16'))

    def ping_tcp(self):
        to_remove = []
        while self.running:
            time.sleep(1)
            for conn in self.connections:
                try:
                    conn.conn.send(bytes("0", 'UTF-16'))
                except ConnectionResetError:
                    conn.conn.close()
                    to_remove.append(conn)
                except BrokenPipeError:
                    conn.conn.close()
                    to_remove.append(conn)
            if len(to_remove) > 0:
                for c in to_remove:
                    self.connections.remove(c)
                to_remove = []
                self.update_nicks()

    def _is_in_connections(self, address) -> bool:
        for conn in self.connections:
            if conn.address[0] == address[0] and conn.udp_port == address[1]:
                return True
        return False

if __name__ == '__main__':
    server = Server(8000,8001, '0.0.0.0')
    server.run()