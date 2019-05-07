# https://cryptopals.com/sets/1/challenges/2
from set1 import BIN_TO_HEX_DICT
from set1.base64enc import hex_to_bytes_iterator

XOR_results = {
    '00': '0',
    '01': '1',
    '10': '1',
    '11': '0',
}


def fixed_xor(hex_str_1: str, hex_str_2: str) -> str:
    bits_str_it_1, bits_str_it_2 = hex_to_bytes_iterator(hex_str_1), hex_to_bytes_iterator(hex_str_2)
    xor_hex_result = ''

    bits_str_buff_1, bits_str_buff_2 = next(bits_str_it_1, None), next(bits_str_it_2, None)
    while bits_str_buff_1 and bits_str_buff_2:
        xor_bits_result_buf = ''
        for bits_char_buff_1, bits_char_buff_2 in zip(bits_str_buff_1, bits_str_buff_2):
            xor_bits_result_buf += XOR_results[bits_char_buff_1 + bits_char_buff_2]
        # The buffer contains 1 byte so 2 hex, this is why we separate the translation in 2 parts
        xor_hex_result += BIN_TO_HEX_DICT[xor_bits_result_buf[:4]] + BIN_TO_HEX_DICT[xor_bits_result_buf[4:]]
        bits_str_buff_1, bits_str_buff_2 = next(bits_str_it_1, None), next(bits_str_it_2, None)

    return xor_hex_result
