import os

from set1.vigenere_decryption import hamming_distance, decrypt_vigenere


def test_hamming_distance_for_equal_str_is_0():
    # GIVEN
    str_1 = 'this is a test'
    str_2 = 'this is a test'

    # WHEN
    actual = hamming_distance(str_1, str_2)

    # THEN
    assert actual == 0


def test_hamming_distance_jake_and_fire_is_6():
    # GIVEN
    str_1 = 'jake'
    str_2 = 'fire'

    # WHEN
    actual = hamming_distance(str_1, str_2)

    # THEN
    assert actual == 6


def test_hamming_distance_for_challenge_is_37_as_described():
    # GIVEN
    str_1 = 'this is a test'
    str_2 = 'wokka wokka!!!'

    # WHEN
    actual = hamming_distance(str_1, str_2)

    # THEN
    assert actual == 37


def test_challenge_should_match():
    # GIVEN
    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = f'{current_dir}/../data/vigenered_text.txt'

    # WHEN
    decrypted_text, key = decrypt_vigenere(filename)

    # THEN
    assert key == 'Terminator X: Bring the noise'
    assert decrypted_text[:33] == 'I\'m back and I\'m ringin\' the bell'
