from set1.repeating_key_xor import xor_with_repeating_key


def test_challenge_should_match():
    # GIVEN
    phrase = 'Burning \'em, if you ain\'t quick and nimble\n' \
             'I go crazy when I hear a cymbal'
    key = 'ICE'

    # WHEN
    actual = xor_with_repeating_key(phrase, key)

    # THEN
    assert actual == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272' \
                     'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'


def test_key_longer_than_input():
    # GIVEN
    phrase = 'ICEICE'
    key = 'Burning \'em, if you ain\'t quick and nimble\n' \
          'I go crazy when I hear a cymbal'

    # WHEN
    actual = xor_with_repeating_key(phrase, key)

    # THEN
    assert actual == '0b3637272a2b'
