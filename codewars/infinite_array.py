def search_infinite_array(n, key):
    start = 0
    end = 0
    i = 1
    while arr[end] < key:
        start = end
        end = 2 ** i
        i += 1
    return binary_search(arr, start, end)
