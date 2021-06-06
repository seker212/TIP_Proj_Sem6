from sys import argv
from client_base import Client

client = Client("127.0.0.1",8000,argv[1])
client.run_client()
#client.get_perticipants()