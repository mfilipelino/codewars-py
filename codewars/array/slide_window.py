def find_max_sliding_window(arr, window_size):
    _max_index1 = 0
    _max_index2 = 0
    arr_size = len(arr)
    for i in range(window_size):  # [3, 2, 1]
        if arr[i] > arr[_max_index1]:
            _max_index2 = _max_index1
            _max_index1 = i

    return _max
