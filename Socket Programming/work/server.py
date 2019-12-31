import socket
import re
import ast
import datetime
from database_helper import db

IP = "127.0.0.1"
PORT = 2021
LOG = open("Logs/socket_server.log", "a")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows to use the same IP/Port on server restart
s.bind((IP, PORT))
s.listen(5)


def log_entry(msg):
    timestamp = "[{}] ".format(datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S"))
    print(timestamp + msg)
    LOG.write(timestamp + msg + "\n")


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


log_entry("Listening for incoming connection at {}:{}".format(IP, PORT))

while True:
    clientsocket, address = s.accept()
    log_entry("Connection from {} has been established!".format(address))
    data = clientsocket.recv(1024).decode("utf-8")
    log_entry("Successfully decoded data received from {}".format(address))
    data = _change_data_to_dict(data)
    if data:
        db_entry = db.enter_data_in_db(data)
        if not (db_entry[0]):
            log_entry("ERROR: Failed to save data recvd from {} | DATA: {}".format(address, db_entry[1]))
            log_entry("{}".format(db_entry[2]))
        elif db_entry[0]:
            log_entry("SUCCESS: Saved data recvd from {} | DATA: {}".format(address, db_entry[1]))
        else:
            log_entry("Unknown event occurred while saving the data recvd from {}".format(address))
