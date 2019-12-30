import socket

HEADER_SIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1236))

while True:
    full_msg = ""
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"New message length: {msg[:HEADER_SIZE]}")
            msg_length = int(msg[:HEADER_SIZE])
            new_msg = False
        decoded_msg = msg.decode("utf-8")
        full_msg += decoded_msg
        if len(full_msg)-HEADER_SIZE == msg_length:
            print("Full message received.")
            print(full_msg[HEADER_SIZE:])
            new_msg = True
            full_msg = ""
    print(full_msg)
