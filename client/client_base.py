import socket
import threading
from audio_module import *

class Client(object):
    def __init__(self) -> None:
        
        self.target_ip = "192.168.56.1"
        self.target_port = "8000"

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(self.target_ip,self.target_port)

        except:
            print('ERROR: Counld\'t connect')
    
        self.audioHelper = AudioHelper()

        self.audioHelper.open_input_stream()
        self.audioHelper.open_output_stream()

        reciver = threading.Thread(target=self.receive_data).start()
        sender = threading.Thread(target=self.send_data).start()

    def receive_data(self):
        while True:
            try:
                data = self.socket.recv(1024)
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