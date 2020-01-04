import re
import ast


def change_data_to_dict(data):
    """
    Extracts a substring surrounded by curly braces from a string passed in the parameter and converts it in to a
    dictionary. If no substring with curly braces is found, it returns None
    :param data: String object received from the client
    :return: Dictionary object
    """
    search_substring = re.search("{([^}]+)}", data)  # Extracts string which starts and ends with curly braces
    if search_substring:
        data_as_string = search_substring.group(0)
        data_dictionary = ast.literal_eval(data_as_string)
        if isinstance(data_dictionary, dict):
            return data_dictionary
