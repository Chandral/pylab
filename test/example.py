def get_my_data(dictionary, threshold):
    """
    Function takes two parameters: A dictionary and a threshold value as an integer.
    """
    if 0 <= threshold <= 100:  # Ensures the threshold value is between 0 to 100 for representing percentage
        """# The line below gets you"""
        threshold = (max([value for value in dictionary.values()])) * (threshold/100)
        merged_keys = ()
        for key, value in dictionary.items():
            if value < threshold:
                merged_keys += key
        return set(letter for letter in merged_keys if merged_keys.count(letter) > 1)
    else:
        return f"Invalid threshold value: {threshold}, please enter a value between 0 to 100."


your_dictionary = {('a', 'b'): 2, ('b', 'c'): 4, ('c', 'd'): 6, ('d', 'e'): 8, ('e', 'f'): 8, ('f', 'g'): 3,
                   ('g', 'h'): 2, ('h', 'i'): 7, ('i', 'j'): 10}
result = get_my_data(your_dictionary, 50)
print(result)