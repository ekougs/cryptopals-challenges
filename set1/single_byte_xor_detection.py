# https://cryptopals.com/sets/1/challenges/4
from typing import List, Optional

from set1.single_byte_xor_decipher import single_byte_decipher, DecipherError, NoPossibleKeyError, UndecipherablePhraseError


def detect_single_byte_cypher(hex_phrases: List[str]) -> Optional[str]:
    phrases_scores = []
    for hex_phrase in hex_phrases:
        try:
            decipher = single_byte_decipher(hex_phrase)
            phrases_scores.append(decipher)
        except DecipherError:
            continue
    return list(map(lambda phrase_score: phrase_score[0], sorted(phrases_scores, key=lambda phrase_score: phrase_score[2])))[0]
