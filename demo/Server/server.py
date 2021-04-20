import socket
import pyaudio
from threading import Thread

HOST = socket.gethostname()
PORT_UDP = 8000
PORT_TCP = 8001
PACKET_SIZE = 1024 * 8

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

class Server(object):
    def __init__(self,tcp_port,udp_port) -> None:
        self.ip = socket.gethostbyname(socket.gethostname())
        self.tcp_port = tcp_port
        self.udp_port = udp_port
        self.running = True

        try:
            self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_sock.bind((self.ip,self.tcp_port))

        except:
            print('ERROR: couln\'t bind port')

        self.connections = []

    def run(self):
        print('Running on: ' + str(self.ip) + ':' + str(self.tcp_port))

        self.tcp_sock.listen(50)

server = Server(8000,8001)
server.run()