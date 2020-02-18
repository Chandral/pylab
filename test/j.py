ref_bit = {
    "dg.45": ['0000', '0001', '0001', '0000'],
    "dg.46": ['0001', '0001', '0001', '0001'],
    "dg.47": ['0001', '0001', '0001', '0001'],
    "dg.48": ['0001', '0001', '0001', '0001'],
    "dg.49": ['0000', '0001', '0001', '0001'],
    "dg.50": ['0001', '0001', '0001', '0001'],
    "dg.51": ['0001', '0001', '0001', '0001'],
    'dg.52': ['0001', '0001', '0001', '0001'],
    'dg.53': ['0001', '0001', '0001', '1111'],
    'dg.54': ['0001', '0001', '0001', '0001'],
    'dg.55': ['0001', '0001', '0001', '0001'],
    'dg.56': ['0001', '0001', '0001', '0001'],
    'dg.57': ['0000', '0000', '0000', '0001'],
    'dg.58': ['0001', '0001', '0001', '0001'],
    'dg.59': ['0001', '1111', '1011', '0101'],
    'dg.60': ['0001', '0000', '0000', '0000'],
    'dg.61': ['0000', '0000', '0001', '0001'],
    'dg.62': ['0001', '0001', '0001', '0001'],
    'dg.64': ['0000', '0000', '0000', '0001'],
    'dg.65': ['0000', '0000', '0001', '0001']
}


def split_binary(binary_string, divided_by):
    """
    This function splits a string of binary digits (e.g. "0100001000001111") into parts of 'divided_by'
    :param binary_string: A string of 0s and 1s
    :param divided_by: An integer for how many 0s and 1s should be in each split
    :return: A list of 0s and 1s where each element in the list will contain 'divided_by' number of bits or less.
    """
    total_length = len(binary_string)
    if total_length < 16:
        add_0 = '0' * (16-total_length)
        binary_string = add_0 + binary_string
    print(">>>>",len(binary_string))
    total_length = len(binary_string)
    total_equal_splits = total_length // divided_by
    remaining_split = total_length % divided_by
    result = []
    if total_equal_splits > 0:
        start = -divided_by
        end = total_length
        for i in range(0, total_equal_splits):
            result.append(binary_string[start:end])
            end = start
            start += -divided_by
        if remaining_split > 0:
            result.append(binary_string[:remaining_split])
    else:
        result.append(binary_string)
    return result


def compare_bits(bit_list, ref_bits):
    ref_bits_index = 0
    result = []
    for bit in bit_list:
        result.append((bit, bit == ref_bits[ref_bits_index], ref_bits[ref_bits_index]))
        ref_bits_index += 1
    return result


sample_bits = '1000100010001'
# bit_list = split_binary(sample_bits, 4)
# ref_list = ref_bit['dg.65']
# a = compare_bits(bit_list, ref_list)
l = len(sample_bits)
if l != 16:
    zeroes = '~' * (16-l)
sample_bits = zeroes + sample_bits
print(len(sample_bits))
print(sample_bits)