from set1.fixed_xor import fixed_xor


def test_challenge_should_match():
    # GIVEN
    hex_str_1 = '1c0111001f010100061a024b53535009181c'
    hex_str_2 = '686974207468652062756c6c277320657965'

    # WHEN
    actual = fixed_xor(hex_str_1, hex_str_2)

    # THEN
    assert actual == '746865206b696420646f6e277420706c6179'
