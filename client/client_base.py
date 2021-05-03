import socket
import sys
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

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.target_ip,self.target_port))
            self.error_message = "Connected"
            self.connected = True

        except Exception as err:
            print('ERROR: Counld\'t connect')
            print(err)
            self.error_message = "Couldn't connect!"
    
        self.audioHelper = AudioHelper()

    def receive_data(self):
        while True:
            try:
                data = self.socket.recv(CHUNK)
                self.audioHelper.audio_output_write(data)
            except Exception as err:
                print(err)

    def send_data(self):
        while True:
            try:
                data = self.audioHelper.audio_input_read()
                print(len(data))
                self.socket.sendall(data)
            except Exception as err:
                print(err)
                sys.exit(1)

    def run_client(self):

        self.audioHelper.open_input_stream()
        self.audioHelper.open_output_stream()

        reciver = threading.Thread(target=self.receive_data).start()
        sender = threading.Thread(target=self.send_data).start()
