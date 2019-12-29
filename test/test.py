import re
import ast
import threading


def _change_data_to_dict(data):
    search_substring = re.search("{([^}]+)}", data)  # Extracts string which starts and ends with curly braces
    if search_substring:
        data_as_string = search_substring.group(0)
        data_dictionary = ast.literal_eval(data_as_string)
        if isinstance(data_dictionary, dict):
            return data_dictionary


def enter_data_in_db(data):
    if _change_data_to_dict(data):
        return True


test_data = "asdfasdfasd {'a': 1, 'b':2}  asdfasd"
my_data = enter_data_in_db(test_data)
print(my_data)

# t1 = threading.Thread(target=enter_data_in_db, args=(test_data,))
# t2 = threading.Thread(target=enter_data_in_db(), args=(test_data,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()