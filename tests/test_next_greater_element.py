from codewars.stack.next_greater_element import next_greater_element


def test_next_greater_element():
    assert next_greater_element([2, 8, 1]) == [8, -1, -1]
    assert next_greater_element([3, 2, 8, 1]) == [8, 8, -1, -1]
    assert next_greater_element([4, 6, 3, 2, 8, 1]) == [6, 8, 8, 8, -1, -1]
    print()
    print(next_greater_element([13, 3, 12, 16, 15, 11, 1, 2]))
