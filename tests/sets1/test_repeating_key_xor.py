from set1 import convert_ascii_to_hex
from set1.repeating_key_xor import xor_ascii_with_repeating_key


def test_challenge_should_match():
    # GIVEN
    phrase = 'Burning \'em, if you ain\'t quick and nimble\n' \
             'I go crazy when I hear a cymbal'
    key = 'ICE'

    # WHEN
    actual = xor_ascii_with_repeating_key(phrase, convert_ascii_to_hex(key))

    # THEN
    assert actual == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272' \
                     'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'


def test_key_longer_than_input():
    # GIVEN
    phrase = 'ICEICE'
    key = 'Burning \'em, if you ain\'t quick and nimble\n' \
          'I go crazy when I hear a cymbal'

    # WHEN
    actual = xor_ascii_with_repeating_key(phrase, convert_ascii_to_hex(key))

    # THEN
    assert actual == '0b3637272a2b'


def test_with_one_char():
    # GIVEN
    phrase = 'Now that the party is jumping\n'
    key = '5'

    # WHEN
    actual = xor_ascii_with_repeating_key(phrase, convert_ascii_to_hex(key))

    # THEN
    assert actual == '7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f'
