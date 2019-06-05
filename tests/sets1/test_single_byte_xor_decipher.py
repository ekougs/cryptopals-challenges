from set1.fixed_xor import fixed_xor
from set1.single_byte_xor_decipher import single_byte_decipher


def test_challenge_should_match():
    # GIVEN
    hex_cyphered_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    # WHEN
    actual = single_byte_decipher(hex_cyphered_str)

    # THEN
    assert actual == 'Cooking MC\'s like a pound of bacon'


def test_on_a_longer_sample():
    # GIVEN
    hex_deciphered_str = '546f6f6c20746f20646563727970742f656e6372797074207769746820584f52206175746f6d61746963616c6c792e20584f522043697068657220697320612063' \
                         '727970746f67726170686963206d6574686f6420646576656c6f706564207769746820636f6d7075746572732e20497320636f6e736973747320696e20656e6372' \
                         '797074696e6720612062696e617279206d65737361676520776974682061207265706561746564206b6579207573696e67206120584f52206d756c7469706c6963' \
                         '6174696f6e2e'
    hex_cyphered_str = fixed_xor(hex_deciphered_str, '42' * (int(len(hex_deciphered_str) / 2)))

    # WHEN
    actual = single_byte_decipher(hex_cyphered_str)

    # THEN
    assert actual == 'Tool to decrypt/encrypt with XOR automatically. XOR Cipher is a cryptographic method developed with computers. Is consists in encrypt' \
                     'ing a binary message with a repeated key using a XOR multiplication.'
