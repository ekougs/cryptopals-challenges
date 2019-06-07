# https://cryptopals.com/sets/1/challenges/4
from typing import List, Optional

from set1 import is_likely_english_text_via_most_frequent_chars, get_most_frequent_chars
from set1.single_byte_xor_decipher import single_byte_decipher, NoPossibleKeyError, UndecipherablePhraseError


def detect_single_byte_cypher(hex_phrases: List[str]) -> Optional[str]:
    for idx, hex_phrase in enumerate(hex_phrases):
        most_frequent_chars_for_phrase: List[str] = get_most_frequent_chars(hex_phrase)
        # It is likely cyphered if it is unlikely to be an english phrase as is
        if is_likely_english_text_via_most_frequent_chars(most_frequent_chars_for_phrase):
            continue
        try:
            deciphered_phrase = single_byte_decipher(hex_phrase)
            print(idx)
            return deciphered_phrase
        except (NoPossibleKeyError, UndecipherablePhraseError):
            continue
    return None
