import re
import ast


def change_data_to_dict(data):
    search_substring = re.search("\{([^}]+)\}", data)  # Extracts string which starts and ends with curly braces
    data_as_string = search_substring.group(0)
    data_dictionary = ast.literal_eval(data_as_string)
    isinstance(my_data, dict)
    return data_dictionary


test_data = "asdfasdfasd {'a': 1, 'b':2} asdfasd"
my_data = change_data_to_dict(test_data)
t = type(my_data)
print(t)
print(isinstance(my_data, dict))
