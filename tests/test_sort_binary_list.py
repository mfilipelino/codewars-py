from codewars.sort_binary_list import sort_binary_list


def test_sort_binary_list():
    assert sort_binary_list([1, 0, 0, 1]) == [0, 0, 1, 1]
    assert sort_binary_list([0]) == [0]
    assert sort_binary_list([1]) == [1]
    assert sort_binary_list([1, 0]) == [0, 1]
