import time
import pickle
import socket

HEADER_SIZE = 10
sample_data = {"Hey": 1, "There": 2}


"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows to use the same IP/Port on server restart
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADER_SIZE}}' + msg
    clientsocket.send(msg.encode('utf-8'))
    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f'{len(msg):<{HEADER_SIZE}}' + msg
        clientsocket.send(msg.encode('utf-8'))
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows to use the same IP/Port on server restart
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    msg = pickle.dumps(sample_data)
    msg = bytes(f'{len(msg):<{HEADER_SIZE}}', 'utf-8') + msg
    clientsocket.send(msg)
