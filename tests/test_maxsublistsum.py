from codewars.maxsublistsum import find_max_sum_sublist


def test_base():
    assert find_max_sum_sublist([5]) == 5
    assert find_max_sum_sublist([1, 6]) == 7
    assert find_max_sum_sublist([1, 6, -2]) == 7
    assert find_max_sum_sublist([1, -6, -2]) == 1
    assert find_max_sum_sublist([-1, -6, -2]) == -1

