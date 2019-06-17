# https://cryptopals.com/sets/1/challenges/6
import base64
import itertools
import operator
from functools import reduce
from statistics import mean
from typing import Iterator, Tuple, List

from set1.repeating_key_xor import xor_ascii_with_repeating_key
from set1.single_byte_xor_decipher import single_byte_decipher


# Credits to https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
def _count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


def hamming_distance(str_1: str, str_2: str) -> int:
    return hamming_distance_bytes(str_1.encode('ascii'), str_2.encode('ascii'))


def hamming_distance_bytes(bytes_1: bytes, bytes_2: bytes):
    ored_bytes = list(itertools.chain([a ^ b for (a, b) in zip(bytes_1, bytes_2)]))
    return sum(map(_count_set_bits, ored_bytes))


def decrypt_vigenere(filename: str) -> Tuple[str, str]:
    with open(filename) as f:
        bytes_buffer = base64.b64decode(f.read())

    normalized_hamming_distances: List[Tuple[int, int]] = []
    for key_size in range(2, 41):
        normalized_hamming_distances.append((key_size, mean(
            map(
                lambda key_sized_adjacent_words: hamming_distance_bytes(key_sized_adjacent_words[0], key_sized_adjacent_words[1]) / key_size,
                map(
                    lambda i: (bytes_buffer[i:i + key_size], bytes_buffer[i + key_size:i + key_size * 2]),
                    range(0, len(bytes_buffer), key_size * 2)
                )
            )
        )))

    key_size = next(
        map(
            lambda indexed_distance: indexed_distance[0],
            sorted(
                normalized_hamming_distances,
                key=lambda indexed_distance: indexed_distance[1]
            )
        )
    )

    key = reduce(
        operator.concat,
        map(
            # We get the key char for each block of the cipher by going through all the range of the key
            lambda hex_sample: single_byte_decipher(hex_sample)[1],
            map(
                lambda idx: bytes_buffer[idx:len(bytes_buffer):key_size].hex(),
                range(key_size)
            )
        )
    )

    decrypted_text_hex = xor_ascii_with_repeating_key(bytes_buffer.decode('ascii'), key.encode('ascii').hex())
    return bytearray.fromhex(decrypted_text_hex).decode(), key


def iter_file(filename: str) -> Iterator[str]:
    with open(filename) as f:
        while True:
            char = f.read(1)
            if not char:
                break
            if char in ['\r', '\n']:
                continue
            yield char
