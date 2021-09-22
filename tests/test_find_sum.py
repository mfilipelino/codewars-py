from codewars.array.find_sum import find_sum


def test_find_sum():
    # case 1
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 81
    assert find_sum(lst, k) == [21, 60]
    # case 2
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 11
    assert find_sum(lst, k) == [5, 6]
    # case 3
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 5
    assert find_sum(lst, k) == None
