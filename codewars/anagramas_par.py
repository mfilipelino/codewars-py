def hash(ss):
    return sum([ord(c) for c in ss])


def anagrama_list(lst):
    anagrama_lst = {}
    for word in lst:
        key = hash(word)
        if key in anagrama_lst:
            anagrama_lst[key].append(word)
        else:
            anagrama_lst[key] = [word]
    return [value for value in anagrama_lst.values()]
