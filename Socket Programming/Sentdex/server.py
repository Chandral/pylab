import socket
import pickle

d = {1: "Hey", 2: "There"}
msg = pickle.dumps(d)
print(msg)




"""
HEADER_SIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1236))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADER_SIZE}}' + msg
    clientsocket.send(bytes(msg, "UTF-8"))
"""
