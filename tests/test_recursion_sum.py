from codewars.recursion_sum import recursion_add


def test_recursion_add_base_base():
    assert recursion_add(0) == 0
    assert recursion_add(1) == 1


def test_recursion_add_cases():
    assert recursion_add(2) == 3
    assert recursion_add(3) == 6
