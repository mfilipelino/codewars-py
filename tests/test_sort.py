from codewars.array.sort import insertion_sort, bubble_sort, merge_sort, merge


def test_insertion_sort_case_base():
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]


def test_insertion_sort():
    assert insertion_sort([1, 2]) == [1, 2]
    assert insertion_sort([2, 1]) == [1, 2]
    assert insertion_sort([3, 2, 1]) == [1, 2, 3]
    assert insertion_sort([3, 2, 1, 4]) == [1, 2, 3, 4]
    assert insertion_sort([3, -2, 1, 4]) == [-2, 1, 3, 4]


def test_bubble_sort_case_base():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]


def test_bubble_sort():
    assert bubble_sort([1, 2]) == [1, 2]
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([3, 2, 1, 4]) == [1, 2, 3, 4]
    assert bubble_sort([3, -2, 1, 4]) == [-2, 1, 3, 4]


def test_merge_sort_case_base():
    assert (
        merge_sort(
            [],
        )
        == []
    )
    assert merge_sort([1]) == [1]


def test_merge_sort():
    assert merge_sort([1, 2]) == [1, 2]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([2, 1, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_merge_function():
    assert merge([1, 2], [1], [2]) == [1, 2]
    assert merge([4, 3, 2, 1], [3, 4], [1, 2]) == [1, 2, 3, 4]
