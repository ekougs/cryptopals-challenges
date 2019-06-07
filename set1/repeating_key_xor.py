from set1 import convert_ascii_to_hex
from set1.fixed_xor import fixed_xor


def xor_with_repeating_key(phrase: str, key: str) -> str:
    hex_phrase = convert_ascii_to_hex(phrase)
    hex_key = convert_ascii_to_hex(key)

    xored_phrase_hex = ''
    # While last character of phrase not encrypted
    phrase_remaining_length = len(hex_phrase)
    key_length = len(hex_key)
    while phrase_remaining_length > 0:
        length_to_xor = min([phrase_remaining_length, key_length])
        xor_start_idx = len(hex_phrase) - phrase_remaining_length
        xored_phrase_hex += fixed_xor(hex_phrase[xor_start_idx:xor_start_idx + length_to_xor], hex_key[:length_to_xor])
        phrase_remaining_length -= length_to_xor
    return xored_phrase_hex
