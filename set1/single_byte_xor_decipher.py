# https://cryptopals.com/sets/1/challenges/3
from mypy.types import Dict, Set

from set1.fixed_xor import fixed_xor

# source https://en.wikipedia.org/wiki/Frequency_analysis
# source https://en.wikipedia.org/wiki/Frequency_analysis#/media/File:English_letter_frequency_(alphabetic).svg
# Usual frequent chars in the english language
frequent_chars_hex: Set[str] = [format(ord(char), 'x') for char in ['e', 't', 'a', 'o', 'i', 'n', ' ', 's', 'h', 'r', 'd', 'l', 'u']]


def single_byte_decipher(hex_str: str) -> str:
    # We first store occurrences of every single letters
    # There is at most 52 of them so the memory space occupied is independent of the input size
    occurrences_by_char: Dict[str, int] = {}

    for char_hex_part_1, char_hex_part_2 in zip(hex_str[0::2], hex_str[1::2]):
        # First we set the number of occurrences for this character
        cur_char = char_hex_part_1 + char_hex_part_2
        if cur_char not in occurrences_by_char:
            occurrences_by_char[cur_char] = 0
        occurrences_by_char[cur_char] += 1

    # We get the most N frequent cyphered chars with N being the size of the frequent chars in english
    # We will use this later to check that most of the frequent chars are encrypted in this list
    most_frequent_cyphered_chars = [
        frequent_char for frequent_char in sorted(occurrences_by_char, key=occurrences_by_char.get, reverse=True)[:len(frequent_chars_hex)]
    ]

    most_frequent_cyphered_char = most_frequent_cyphered_chars[0]
    potential_hex_key = ''
    # The most frequent cyphered char matches at least with one of the usual frequent chars above
    # So we iterate through them to find potential keys by XORing the frequent char and its potential cyphered match
    for frequent_char_hex in frequent_chars_hex:
        potential_hex_key = fixed_xor(frequent_char_hex, most_frequent_cyphered_char)
        # We decipher the most frequent cyphered keys with our potential key
        # We check then that it is a likely key by checking if there is enough intersections between the usual frequent chars above and
        # the ones we deciphered otherwise it is highly unlikely that we found the key
        deciphered_most_frequent_chars = [fixed_xor(frequent_char_hex, potential_hex_key) for frequent_char_hex in most_frequent_cyphered_chars]
        if len(list(set(deciphered_most_frequent_chars) & set(frequent_chars_hex))) >= (len(frequent_chars_hex) / 2):
            break

    complete_key = ''.join(potential_hex_key * (int(len(hex_str) / 2)))
    return bytearray.fromhex(fixed_xor(hex_str, complete_key)).decode()
