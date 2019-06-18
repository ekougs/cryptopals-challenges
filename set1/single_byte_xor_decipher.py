# https://cryptopals.com/sets/1/challenges/3
import sys
from typing import Tuple, Dict, List

from set1.fixed_xor import fixed_xor
from set1.repeating_key_xor import xor_hex_with_repeating_key


def single_byte_decipher(hex_str: str) -> Tuple[str, str, int]:
    bytes_length = len(hex_str) / 2

    encrypted_char_frequencies = _get_chars_occurrences(hex_str)

    min_score = sys.maxsize
    potential_hex_key = ''
    for dec_key in range(256):
        hex_key = '{:02x}'.format(dec_key)
        score = _get_chi2(encrypted_char_frequencies, bytes_length, dec_key)
        if min_score > score:
            min_score = score
            potential_hex_key = hex_key

    if not potential_hex_key:
        raise NoPossibleKeyError()

    return bytearray.fromhex(xor_hex_with_repeating_key(hex_str, potential_hex_key)).decode(), bytearray.fromhex(potential_hex_key).decode(), min_score


class NoPossibleKeyError(Exception):
    pass


def _get_chars_occurrences(hex_str: str) -> Dict[int, int]:
    # We first store occurrences of every single letters
    # There is at most 52 of them so the memory space occupied is independent of the input size
    chars_occurrences: Dict[int, int] = {}

    # First we set the number of occurrences for every characters in the string
    for char_hex_part_1, char_hex_part_2 in zip(hex_str[0::2], hex_str[1::2]):
        cur_char = int(char_hex_part_1 + char_hex_part_2, 16)
        if cur_char not in chars_occurrences:
            chars_occurrences[cur_char] = 0
        chars_occurrences[cur_char] += 1

    # We then get the most N frequent chars with N being the size of the frequent chars in english
    return chars_occurrences


# https://crypto.stackexchange.com/questions/30209/developing-algorithm-for-detecting-plain-text-via-frequency-analysis
# The lower the score, the most likely the phrase is in english
# Because it is basically the sum of differences between expected number of occurrences of the chars in english and actual occurrences
def _get_chi2(str_char_occurrences, str_len, key: int):
    # if some non printable ascii characters, it gets max possible score as it certainly is not english
    if any((c not in _printable_ascii_dec_encrypted_codes[key] for c in str_char_occurrences)):
        return sys.maxsize

    chi2 = 0

    cur_letters_ascii_encrypted_dec_codes = _letters_ascii_encrypted_dec_codes[key]
    cur_english_encrypt_freq = _english_encrypt_freq[key]
    for i in cur_letters_ascii_encrypted_dec_codes:
        observed = 0
        # We add lower and upper occurrences and then delete them in the char occurrences dict
        for j in [j for j in [i, i + 32] if j in str_char_occurrences]:
            observed += str_char_occurrences[j]

        expected = str_len * cur_english_encrypt_freq[i]
        difference = observed - expected
        chi2 += difference * difference / expected

    for punct_encrypt_char in (
            punct_encrypt_char
            for punct_encrypt_char in cur_english_encrypt_freq
            if punct_encrypt_char not in cur_letters_ascii_encrypted_dec_codes
    ):
        observed = str_char_occurrences[punct_encrypt_char] if punct_encrypt_char in str_char_occurrences else 0
        expected = str_len * cur_english_encrypt_freq[punct_encrypt_char]
        difference = observed - expected
        chi2 += difference * difference / expected

    # We add to the difference score chi2 the other non word characters
    # Their expected frequency is not known but I fixed it to 100 times lower than any word character
    # As they are highly unlikely to appear in an english text
    expected_other_chars = 0.0000074 * str_len
    for char in (char for char in str_char_occurrences if char not in _evaluated_freq_ascii_dec_encrypted_codes[key]):
        observed = str_char_occurrences[char]
        difference = observed - expected_other_chars
        chi2 += difference * difference / expected_other_chars

    return chi2


# http://en.algoritmy.net/article/40379/Letter-frequency-English
# https://en.wikipedia.org/wiki/Punctuation_of_English#Frequency
_english_char_frequencies = {
    # A-Z
    65: 0.08167, 66: 0.01492, 67: 0.02782, 68: 0.04253, 69: 0.12702, 70: 0.02228, 71: 0.02015,
    72: 0.06094, 73: 0.06966, 74: 0.00153, 75: 0.00772, 76: 0.04025, 77: 0.02406, 78: 0.06749,
    79: 0.07507, 80: 0.01929, 81: 0.00095, 82: 0.05987, 83: 0.06327, 84: 0.09056, 85: 0.02758,
    86: 0.00978, 87: 0.02360, 88: 0.00150, 89: 0.01974, 90: 0.00074,
    # Punctuation and space
    32: 0.12702,  # space -> In English, the space is slightly more frequent than the top letter (e) [https://en.wikipedia.org/wiki/Letter_frequency]
    46: 0.0653,  # full stop
    44: 0.0613,  # comma
    59: 0.0032,  # semicolon
    58: 0.0034,  # colon
    33: 0.0033,  # exclamation mark
    63: 0.0056,  # question mark
    39: 0.0243,  # apostrophe / single quotation mark
    34: 0.0267,  # double quotation mark
    45: 0.0153  # hyphen
}
_letters_ascii_dec_codes = list(range(65, 91))

# (TAB, CR, LF, numbers, punct, space, or letters)
_evaluated_freq_ascii_dec_codes = [9, 10, 13]
_evaluated_freq_ascii_dec_codes.extend(_english_char_frequencies.keys())
_evaluated_freq_ascii_dec_codes.extend(list(range(97, 123)))

_printable_ascii_dec_codes = [9, 10, 13]
_printable_ascii_dec_codes.extend(list(range(32, 127)))

# To speed up algorithms that run multiple times chi2, we compute the encrypted counterparts of our variables
# For one of the test we get a factor of 5 between this version and the version where for each key the hex phrase keys are decrypted
_english_encrypt_freq: List[dict] = []
_letters_ascii_encrypted_dec_codes: List[List[int]] = []
_evaluated_freq_ascii_dec_encrypted_codes: List[List[int]] = []
_printable_ascii_dec_encrypted_codes: List[List[int]] = []
for _dec_key in range(256):
    _hex_key = '{:02x}'.format(_dec_key)
    _english_encrypt_freq.append({int(fixed_xor('{:02x}'.format(k), _hex_key), 16): _english_char_frequencies[k] for k in _english_char_frequencies})
    _letters_ascii_encrypted_dec_codes.append([int(fixed_xor('{:02x}'.format(k), _hex_key), 16) for k in _letters_ascii_dec_codes])
    _evaluated_freq_ascii_dec_encrypted_codes.append([int(fixed_xor('{:02x}'.format(k), _hex_key), 16) for k in _evaluated_freq_ascii_dec_codes])
    _printable_ascii_dec_encrypted_codes.append([int(fixed_xor('{:02x}'.format(k), _hex_key), 16) for k in _printable_ascii_dec_codes])
