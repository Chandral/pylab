import socket
import re
import ast
import datetime
from database_helper import db

IP = "127.0.0.1"
PORT = 2021
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows to use the same IP/Port on server restart
s.bind((IP, PORT))
s.listen(5)


def _change_data_to_dict(data):
    """
    Private function which accepts a string then extracts a substring surround by curly braces and converts it to
    dictionary. This function is not used directly, it's used within another function 'enter_data_in_db()'
    :param data: String object received from the client
    :return: Dictionary object
    """
    search_substring = re.search("{([^}]+)}", data)  # Extracts string which starts and ends with curly braces
    if search_substring:
        data_as_string = search_substring.group(0)
        data_dictionary = ast.literal_eval(data_as_string)
        if isinstance(data_dictionary, dict):
            return data_dictionary


while True:
    clientsocket, address = s.accept()
    print("Connection from has been established!")
    data = clientsocket.recv(1024).decode("utf-8")
    data = _change_data_to_dict(data)
    if data:
        db.enter_data_in_db(data)
