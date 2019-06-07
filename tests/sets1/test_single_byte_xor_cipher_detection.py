import os

from set1.single_byte_xor_detection import detect_single_byte_cypher


def test_challenge_should_match():
    # GIVEN
    hex_phrases = _get_data_file_lines('with_cyphered_phrase_but_no_english_phrase')

    # WHEN
    actual = detect_single_byte_cypher(hex_phrases)

    # THEN
    assert actual == 'Now that the party is jumping\n'


def test_containing_english_phrase():
    # GIVEN
    hex_phrases = _get_data_file_lines('with_cyphered_phrase_and_english_phrase')

    # WHEN
    actual = detect_single_byte_cypher(hex_phrases)

    # THEN
    assert actual == 'Now that the party is jumping\n'


def test_no_encrypted_phrase():
    # GIVEN
    hex_phrases = _get_data_file_lines('without_cyphered_phrase')

    # WHEN
    actual = detect_single_byte_cypher(hex_phrases)

    # THEN
    assert actual is None


def _get_data_file_lines(filename):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_dir}/../data/{filename}.txt') as f:
        return [hex_phrase.strip() for hex_phrase in f.readlines()]
