import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025))
s.listen(5)  # Number of client connections allowed at a time?

while True:
    clt, adr = s.accept()  # clt is the object of client's socket and adr is a tuple of IP:Port correct?
    print(f"Connection to {adr} established")
    clt.send(bytes("Socket Programming in Python", "UTF-8"))  # Server byte limit???
    clt.close()  # The connection stays active even when I have terminated this program in CLI??
