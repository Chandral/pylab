import socket
import pickle

a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2133))

while True:
    complete_data = b''
    rec_msg = True
    while True:
        my_msg = s.recv(16)  # Total length of the message can be found in the first packet of 16?
        if rec_msg:
            print(f"The length of the message = {my_msg[:a]}")
            x = int(my_msg[:a])
            rec_msg = False
        complete_data += my_msg
        if len(complete_data)-a == x:
            print("Received complete info")
            print(complete_data[a:])  # Why is 'a' in the beginning here?
            m = pickle.loads(complete_data[a:])
            print("~~~~~", m)
            rec_msg = True
            complete_data = b''
    print("*****", complete_data)
