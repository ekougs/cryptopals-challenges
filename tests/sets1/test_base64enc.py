import pytest

from set1.base64enc import hex_to_base64


def test_base64_encoding_padding_once():
    # GIVEN
    hex_str = '4d61'

    # WHEN
    actual = hex_to_base64(hex_str)

    # THEN
    assert actual == 'TWE='


def test_base64_encoding_padding_twice():
    # GIVEN
    hex_str = '4d'

    # WHEN
    actual = hex_to_base64(hex_str)

    # THEN
    assert actual == 'TQ=='


def test_challenge_should_match():
    # GIVEN
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

    # WHEN
    actual = hex_to_base64(hex_str)

    # THEN
    assert actual == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
