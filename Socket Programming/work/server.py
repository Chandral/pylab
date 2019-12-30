import socket
import re
import ast

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 2023))
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


def enter_data_in_db(data):
    """
    Accepts a string and converts it into a dictionary using the private function '_change_data_to_dict()' and later
    enters the data into the database.
    :param data: String object received from the client
    :return: Dictionary object
    """
    data_dictionary = _change_data_to_dict(data)
    if data_dictionary:
        return data_dictionary


while True:
    clientsocket, address = s.accept()
    print("Connection from has been established!")
    data = clientsocket.recv(1024).decode("utf-8")
    data = enter_data_in_db(data)
    print(type(data))
    print(data)
