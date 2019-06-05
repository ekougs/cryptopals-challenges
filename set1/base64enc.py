# https://cryptopals.com/sets/1/challenges/1

from typing import Iterator

from set1 import HEX_TO_BIN_DICT

_bin_to_base_64_dict = {
    '000000': 'A',
    '000001': 'B',
    '000010': 'C',
    '000011': 'D',
    '000100': 'E',
    '000101': 'F',
    '000110': 'G',
    '000111': 'H',
    '001000': 'I',
    '001001': 'J',
    '001010': 'K',
    '001011': 'L',
    '001100': 'M',
    '001101': 'N',
    '001110': 'O',
    '001111': 'P',
    '010000': 'Q',
    '010001': 'R',
    '010010': 'S',
    '010011': 'T',
    '010100': 'U',
    '010101': 'V',
    '010110': 'W',
    '010111': 'X',
    '011000': 'Y',
    '011001': 'Z',
    '011010': 'a',
    '011011': 'b',
    '011100': 'c',
    '011101': 'd',
    '011110': 'e',
    '011111': 'f',
    '100000': 'g',
    '100001': 'h',
    '100010': 'i',
    '100011': 'j',
    '100100': 'k',
    '100101': 'l',
    '100110': 'm',
    '100111': 'n',
    '101000': 'o',
    '101001': 'p',
    '101010': 'q',
    '101011': 'r',
    '101100': 's',
    '101101': 't',
    '101110': 'u',
    '101111': 'v',
    '110000': 'w',
    '110001': 'x',
    '110010': 'y',
    '110011': 'z',
    '110100': '0',
    '110101': '1',
    '110110': '2',
    '110111': '3',
    '111000': '4',
    '111001': '5',
    '111010': '6',
    '111011': '7',
    '111100': '8',
    '111101': '9',
    '111110': '+',
    '111111': '/',
}


def hex_to_bytes_iterator(hex_str: str) -> Iterator[str]:
    while hex_str:
        yield HEX_TO_BIN_DICT[hex_str[0]] + HEX_TO_BIN_DICT[hex_str[1]]
        hex_str = hex_str[2:]


def hex_to_base64(hex_str: str) -> str:
    # Algo based on https://en.wikipedia.org/wiki/Base64
    base64_translation = ''

    bytes_iterator = hex_to_bytes_iterator(hex_str)
    bits_buffer = next(bytes_iterator, '')
    last_sextet_has_been_padded = False
    nb_of_sextets = 0

    while bits_buffer:
        # Base64 is translated by sextets
        nb_of_sextets += 1
        bits_buffer_length = len(bits_buffer)
        if bits_buffer_length >= 6:
            bits_str_to_decode, bits_buffer = bits_buffer[:6], bits_buffer[6:]
        else:
            # Pad the last bits to get a sextet to decode
            bits_str_to_decode, bits_buffer = bits_buffer + ('0' * (6 - bits_buffer_length)), ''
            last_sextet_has_been_padded = True
        base64_translation += _bin_to_base_64_dict[bits_str_to_decode]
        bits_buffer += next(bytes_iterator, '')

    # Complete the padding
    if last_sextet_has_been_padded:
        # For padding reference, have a look at the last 2 examples in the linked Wikipedia
        nb_of_translated_bytes = nb_of_sextets * 6
        # The number of bits to have complete bytes is the next common multiple of 8 and 6
        nb_of_bits_to_have_complete_bytes = nb_of_translated_bytes + 6
        while nb_of_bits_to_have_complete_bytes % 8 != 0:
            nb_of_bits_to_have_complete_bytes += 6
        nb_of_padding_zeros_to_have_complete_bytes_and_sextets = nb_of_bits_to_have_complete_bytes - nb_of_translated_bytes
        nb_of_padding_equals = int(nb_of_padding_zeros_to_have_complete_bytes_and_sextets / 6)
        base64_translation += '=' * nb_of_padding_equals

    return base64_translation
