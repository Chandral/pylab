import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, 0)
addr_and_port = ('192.168.1.123', 8001)
s.bind(addr_and_port)