import re
import ast
import socket
from helper.logger import enter_log
from helper.db import enter_data_in_db

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


enter_log("INFO", "Listening for incoming connections at {}:{}".format(IP, PORT))

while True:
    clientsocket, address = s.accept()
    enter_log("SUCCESS", "Established incoming connection from {}".format(address))
    data = clientsocket.recv(1024).decode("utf-8")
    enter_log("SUCCESS", "Decoded data received from {}".format(address))
    enter_log("INFO", data)
    data = _change_data_to_dict(data)
    if data:
        db_entry = enter_data_in_db(data)
        if db_entry[0]:
            enter_log("SUCCESS", "Saved data received from {}".format(address))
        elif not db_entry[0]:
            enter_log("ERROR", "Failed to save data received from {}".format(address))
            enter_log("ERROR", db_entry[1])
    else:
        enter_log("WARNING", "Client request does not contain appropriate data")
