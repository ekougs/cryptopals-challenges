# https://cryptopals.com/sets/1/challenges/3
from typing import Optional

from set1 import FREQUENT_CHARS_HEX, is_likely_english_text_via_most_frequent_chars, get_most_frequent_chars
from set1.fixed_xor import fixed_xor


def single_byte_decipher(hex_str: str) -> str:
    # We will use this later to check that most of the frequent chars are encrypted in this list
    most_frequent_cyphered_chars = get_most_frequent_chars(hex_str)

    most_frequent_cyphered_char = most_frequent_cyphered_chars[0]
    potential_hex_key = ''
    deciphered = False
    # The most frequent cyphered char matches at least with one of the usual frequent chars above
    # So we iterate through them to find potential keys by XORing the frequent char and its potential cyphered match
    for frequent_char_hex in FREQUENT_CHARS_HEX:
        potential_hex_key = fixed_xor(frequent_char_hex, most_frequent_cyphered_char)
        # We decipher the most frequent cyphered keys with our potential key
        # We check then that it is a likely key by checking if there is enough intersections between the usual frequent chars above and
        # the ones we deciphered otherwise it is highly unlikely that we found the key
        deciphered_most_frequent_chars = [fixed_xor(frequent_char_hex, potential_hex_key) for frequent_char_hex in most_frequent_cyphered_chars]
        if is_likely_english_text_via_most_frequent_chars(deciphered_most_frequent_chars):
            deciphered = True
            break

    if not deciphered:
        raise NoPossibleKeyError()

    complete_key = ''.join(potential_hex_key * (int(len(hex_str) / 2)))
    try:
        return bytearray.fromhex(fixed_xor(hex_str, complete_key)).decode()
    except UnicodeDecodeError:
        raise UndecipherablePhraseError()


class NoPossibleKeyError(Exception):
    pass


class UndecipherablePhraseError(Exception):
    pass
