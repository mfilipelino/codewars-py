def find_max_sum_sublist(lst):
    _max_sum = lst[0]
    size = len(lst)
    for i in range(0, size, 1):
        s = lst[i]
        if s > _max_sum:
            _max_sum = s
        for j in range(i + 1, size, 1):
            s += lst[j]
            if s > _max_sum:
                _max_sum = s
    return _max_sum
