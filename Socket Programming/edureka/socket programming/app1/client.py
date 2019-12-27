import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1025))  # Bind on server and connect on client????
complete_data = ""
while True:
    msg = s.recv(7)
    if len(msg) == 0:
        break
    complete_data += msg.decode("UTF-8")

print(complete_data)
