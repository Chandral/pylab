import socket
import pickle

a = 10  # What's the header size in this case?
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2133))
s.listen(5)

while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} established")
    m = {1: "Client", 2: "Server"}
    my_msg = pickle.dumps(m)
    my_msg = bytes(f"{len(my_msg):<{a}}", "utf-8") + my_msg  # Totally lost here, didn't pickle turn it to byte code already? Why is it sending in "UTF-8"
    clt.send(my_msg)

