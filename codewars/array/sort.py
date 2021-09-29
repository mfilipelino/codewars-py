def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n + 1, 1):
        for j in range(0, n - i, 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(0, n, 1):
        min = i
        for j in range(i + 1, n, 1):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr


"""
[3, 2, 1] | min = 0 | i = 0 |  j = 1 | arr[j] < arr[min]
[3, 2, 1] | min = 1 | i = 0 |  j = 2 | arr[j] < arr[min]
[3, 2, 1] | min = 2 | i = 0 |  j = 3 | arr[j] < arr[min]
[1, 2, 3] | min = 1 | i = 0 |  j = 3 | arr[j] < arr[min]
[1, 2, 3] | min = 1 | i = 1 |  j = 2 | arr[j] < arr[min]
[1, 2, 3] | min = 2 | i = 1 |  j = 2 | arr[j] < arr[min]
[1, 2, 3] | min = 2 | i = 2 |  j = 3 | arr[j] < arr[min]
"""


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i
        while j > 0 and value < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = value
    return arr


"""
insertion_sort([1, 2])
arr = [1, 2] | n = 2 | i = 1 | j = 1 | value = 2

insertion_sort([2, 1])
arr = [2, 1] | n = 2 | i = 1 | j = 1 | value = 1
arr = [2, 2] | n = 2 | i = 1 | j = 0 | value = 1 
arr = [1, 2] | n = 2 | i = 1 | j = 0 | value = 1 
"""


def merge(arr, left, right):
    arr_n = len(arr)
    left_n = len(left)
    right_n = len(right)
    i = 0
    j = 0
    k = 0
    while i < left_n and j < right_n:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < left_n:
        arr[k] = left[i]
        i += 1
        k += 1

    while k < right_n:
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


"""
merge([3, 4, 1, 2])
arr = [3, 4, 1, 2] | a = 0 | end_a = 2 | b = 2 | end_b = 4
arr = [1, 4, 3, 2] | a = 1 | end_a = 2 | b = 2 | end_b = 4
arr = [1, 4, 3, 2] | a = 1 | end_a = 2 | b = 2 | end_b = 4
arr = [1, 3, 4, 2] | a = 2 | end_a = 2 | b = 2 | end_b = 4
arr 

merge([3, 1, 2])
arr = [3, 1, 2] | a = 0 | end_a = 1 | b = 1 | end_b = 3
arr = [1, 3, 2] | a = 1 | end_a = 1 | b = 1 | end_b = 3
arr = [1, 3, 2] | a = 1 | end_a = 1 | b = 2 | end_b = 3
arr = [1, 2, 3] | a = 2 | end_a = 1 | b = 2 | end_b = 



merge([1, 2, 3])
arr = [1, 2, 3] | a = 0 | end_a = 1 | b = 1 | end_b = 3
arr = [1, 2, 3] | a = 0 | end_a = 1 | b = 2 | end_b = 3
arr = [1, 2, 3] | a = 0 | end_a = 1 | b = 2 | end_b = 3
arr = [1, 2, 3] | a = 0 | end_a = 1 | b = 3 | end_b = 3



merge([3, 2])
arr = [3, 2] | a = 0 | end_a = 1 | b = 1 | end_b = 2
arr = [2, 3] | a = 1 | end_a = 1 | b = 1 | end_b = 2


merge([2, 3])
arr = [2, 3] | a = 0 | end_a = 1 | b = 1 | end_b = 2
arr = [2, 3] | a = 0 | end_a = 1 | b = 2 | end_b = 2





"""


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        middle = n // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(arr, left, right)
