import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows to use the same IP/Port on server restart
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send("Welcome to the server".encode())
    clientsocket.close()