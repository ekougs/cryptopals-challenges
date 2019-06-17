# https://cryptopals.com/sets/1/challenges/5
from typing import Callable

from set1 import convert_ascii_to_hex
from set1.fixed_xor import fixed_xor


def xor_ascii_with_repeating_key(ascii_phrase: str, hex_key: str) -> str:
    return _xor_with_repeating_key(ascii_phrase, hex_key, lambda phrase: len(phrase) * 2, lambda hex_length_to_xor: int(hex_length_to_xor / 2),
                                   lambda phrase_portion: convert_ascii_to_hex(phrase_portion))


def xor_hex_with_repeating_key(hex_phrase: str, hex_key: str) -> str:
    return _xor_with_repeating_key(hex_phrase, hex_key, lambda phrase: len(phrase), lambda hex_length_to_xor: hex_length_to_xor)


def _xor_with_repeating_key(phrase: str, hex_key: str, remaining_phrase_len_fn: Callable[[str], int], phrase_len_to_xor_fn: Callable[[int], int],
                            optional_conversion_fn: Callable[[str], str] = None) -> str:
    xored_phrase_hex = ''
    key_length = len(hex_key)
    # While last character of phrase not XORed
    while phrase:
        hex_length_to_xor = min([remaining_phrase_len_fn(phrase), key_length])
        char_length_to_xor = phrase_len_to_xor_fn(hex_length_to_xor)
        converted_phrase = optional_conversion_fn(phrase[:char_length_to_xor]) if optional_conversion_fn else phrase[:char_length_to_xor]
        xored_phrase_hex += fixed_xor(converted_phrase, hex_key[:hex_length_to_xor])
        phrase = phrase[char_length_to_xor:] if char_length_to_xor < len(phrase) else ''
    return xored_phrase_hex
