#TODO encoding
#TODO logout
#TODO mute

import socket
import sys, time
import threading
from audio_module import *
from settings import CHUNK

class Client(object):
    def __init__(self,target_ip,target_port,nick) -> None:
        
        self.target_ip = target_ip
        self.target_port = target_port
        self.error_message = ""
        self.nick = nick
        self.connected = False
        self.other_participants = []
        self.target_udp_port = None
        self.muted = False

        try:
            self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_socket.connect((self.target_ip,self.target_port))
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_socket.bind(("127.0.0.1", 0)) #FIXME: IP Address
            self.udp_port = self.udp_socket.getsockname()[1]

        except Exception as err:
            print('ERROR: Counld\'t connect')
            print(err)
            self.error_message = "Couldn't connect!"
            sys.exit(1)

        try:
            self.tcp_socket.sendall(bytes(f"{self.nick}:{self.udp_port}", 'UTF-16'))
            approve = self.tcp_socket.recv(CHUNK)
            approve = str(approve, 'UTF-16').split(":")
            if(approve[0] == "ack"):
                self.target_udp_port = int(approve[1])
                self.error_message = "Connected\nUDP Port:" + str(self.udp_port)
                self.connected = True
            elif(approve[0] == "ful"):
                self.error_message = "Server is full!"
            elif(approve[0] == "nak"):
                self.error_message = "Nick already taken!"

        except Exception as err:
            print(err)
            self.error_message = "Some error occured!"
            sys.exit(1)

        print(self.error_message)
        self.audioHelper = AudioHelper()

        #Test
        reciver = threading.Thread(target=self.get_perticipants).start()

    def receive_data(self):
        while True:
            try:
                data = self.udp_socket.recv(4096)
                self.audioHelper.audio_output_write(data)
            except Exception as err:
                print(err)
                sys.exit(1)

    def send_data(self):
        while True:
            if not self.muted:
                try:
                    data = self.audioHelper.audio_input_read()
                    # print(len(data))
                    self.udp_socket.sendto(data, (self.target_ip, self.target_udp_port))
                except Exception as err:
                    print(err)
                    sys.exit(1)

    def run_client(self):

        self.audioHelper.open_input_stream()
        self.audioHelper.open_output_stream()

        reciver = threading.Thread(target=self.receive_data).start()
        sender = threading.Thread(target=self.send_data).start()

    def get_perticipants(self):
        while self.connected:
            data = self.tcp_socket.recv(CHUNK)
            if(str(data,'UTF-16') == "new"):
                self.other_participants.clear()
                while True: 
                    data = self.tcp_socket.recv(CHUNK)
                    data = str(data,'UTF-16')
                    if(data == self.nick):
                        continue
                    elif(data == "fin"):
                        break
                    else:
                        self.other_participants.append(data)

    def mute(self):
        self.muted = not self.muted

if __name__ == '__main__':
    c = Client("127.0.0.1",8000,"Tester3")
    c.run_client()