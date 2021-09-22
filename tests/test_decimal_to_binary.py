from codewars.decimal_to_binary import decimal_to_binary


def test_decimal_to_binary_base():
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(1) == "1"


def test_decimal_to_binary():
    assert decimal_to_binary(2) == "10"
    assert decimal_to_binary(3) == "11"
    assert decimal_to_binary(4) == "100"
    assert decimal_to_binary(11) == "1011"
