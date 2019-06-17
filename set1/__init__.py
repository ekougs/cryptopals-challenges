import binascii
from typing import List

# source https://en.wikipedia.org/wiki/Frequency_analysis
# source https://en.wikipedia.org/wiki/Frequency_analysis#/media/File:English_letter_frequency_(alphabetic).svg
# Usual frequent chars in the english language
FREQUENT_CHARS = ['e', 't', 'a', 'o', 'i', 'n', ' ', 's', 'h', 'r', 'd', 'l', 'u']
FREQUENT_CHARS_HEX: List[str] = [format(ord(char), 'x') for char in FREQUENT_CHARS]

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
for hex_str, bits in HEX_TO_BIN_DICT.items():
    BIN_TO_HEX_DICT[bits] = hex_str


def convert_ascii_to_hex(chars: str) -> str:
    return str(binascii.hexlify(chars.encode('ascii')), 'ascii')
