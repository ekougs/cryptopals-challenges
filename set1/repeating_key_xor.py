from set1 import convert_ascii_to_hex
from set1.fixed_xor import fixed_xor


def xor_with_repeating_key(phrase: str, key: str) -> str:
    hex_key = convert_ascii_to_hex(key)

    xored_phrase_hex = ''
    key_length = len(hex_key)
    # While last character of phrase not XORed
    while phrase:
        # 1 char translates to 2 hex digits, explaining the times and divided by 2 operations below
        hex_length_to_xor = min([len(phrase) * 2, key_length])
        char_length_to_xor = int(hex_length_to_xor / 2)
        xored_phrase_hex += fixed_xor(convert_ascii_to_hex(phrase[:char_length_to_xor]), hex_key[:hex_length_to_xor])
        phrase = phrase[char_length_to_xor:] if char_length_to_xor < len(phrase) else ''
    return xored_phrase_hex
