import binascii
from typing import Dict, List

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
for hex, bits in HEX_TO_BIN_DICT.items():
    BIN_TO_HEX_DICT[bits] = hex


def convert_ascii_to_hex(chars: str) -> str:
    return str(binascii.hexlify(chars.encode('ascii')), 'ascii')


def get_most_frequent_chars(hex_str: str) -> List[str]:
    # We first store occurrences of every single letters
    # There is at most 52 of them so the memory space occupied is independent of the input size
    occurrences_by_char: Dict[str, int] = {}

    # First we set the number of occurrences for every characters in the string
    for char_hex_part_1, char_hex_part_2 in zip(hex_str[0::2], hex_str[1::2]):
        cur_char = char_hex_part_1 + char_hex_part_2
        if cur_char not in occurrences_by_char:
            occurrences_by_char[cur_char] = 0
        occurrences_by_char[cur_char] += 1

    # We then get the most N frequent chars with N being the size of the frequent chars in english
    return [
        frequent_char for frequent_char in sorted(occurrences_by_char, key=occurrences_by_char.get, reverse=True)[:len(FREQUENT_CHARS_HEX)]
    ]


def is_likely_english_text_via_most_frequent_chars(most_frequent_chars: List[str]):
    # It is likely an english text if the size of the intersection between english frequent chars and the input most frequent chars
    # is greater than half of the size of the english frequent chars set size
    # Intersection ==> set(most_frequent_chars) & set(FREQUENT_CHARS_HEX)
    return len(list(set(most_frequent_chars) & set(FREQUENT_CHARS_HEX))) > (len(FREQUENT_CHARS_HEX) / 2)
