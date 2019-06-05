HEX_TO_BIN_DICT = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111',
}

BIN_TO_HEX_DICT = {}
for hex, bits in HEX_TO_BIN_DICT.items():
    BIN_TO_HEX_DICT[bits] = hex


def from_chars_to_hex_list(chars):
    return [format(ord(char), 'x') for char in chars]
