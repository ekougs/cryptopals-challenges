import os

from set1.single_byte_xor_detection import detect_single_byte_cypher


def test_challenge_should_match():
    # GIVEN
    hex_phrases = _get_data_file_lines('with_cyphered_phrase_but_no_english_phrase')

    # WHEN
    actual = detect_single_byte_cypher(hex_phrases)

    # THEN
    assert actual == 'Now that the party is jumping\n'


def _get_data_file_lines(filename):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_dir}/../data/{filename}.txt') as f:
        return [hex_phrase.strip() for hex_phrase in f.readlines()]
