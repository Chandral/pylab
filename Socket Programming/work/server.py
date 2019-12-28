import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 2021))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Connection from has been established!")
    data = clientsocket.recv(1024)
    print(data)