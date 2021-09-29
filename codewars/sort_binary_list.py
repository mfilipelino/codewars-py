def sort_binary_list(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        if lst[j] == 1:
            j -= 1
        elif lst[j] == 0 and lst[i] == 1:
            lst[j], lst[i] = lst[i], lst[j]
        elif lst[i] == 0:
            i += 1
    return lst
