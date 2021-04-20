import socket
import sys
import threading
from audio_module import *
from settings import CHUNK

class Client(object):
    def __init__(self) -> None:
        
        self.target_ip = "127.0.0.1"
        self.target_port = 8000

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.target_ip,self.target_port))

        except Exception as err:
            print('ERROR: Counld\'t connect')
            print(err)
            sys.exit(1)
    
        self.audioHelper = AudioHelper()

        self.audioHelper.open_input_stream()
        self.audioHelper.open_output_stream()

        reciver = threading.Thread(target=self.receive_data).start()
        sender = threading.Thread(target=self.send_data).start()

    def receive_data(self):
        while True:
            try:
                data = self.socket.recv(CHUNK)
                self.audioHelper.audio_output_read(data)
            except:
                pass

    def send_data(self):
        while True:
            try:
                data = self.audioHelper.audio_input_read()
                self.socket.sendall(data)
            except:
                pass