import socket
import pickle

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

"""
while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(HEADER_SIZE)
        if new_msg:
            msg_len = int(msg[:HEADER_SIZE].decode())
            print(msg_len)
            new_msg = False
            continue
        full_msg += msg.decode()
        if len(full_msg) == msg_len:
            break

    print(full_msg)
"""

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(HEADER_SIZE)
        if new_msg:
            msg_len = int(msg[:HEADER_SIZE].decode())
            print(msg_len)
            new_msg = False
            continue
        full_msg += msg
        if len(full_msg) == msg_len:
            print(full_msg)
            break

    print(pickle.loads(full_msg))