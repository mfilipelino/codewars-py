def find_sum(arr, k):
    size = len(arr)
    arr.sort()
    left = 0
    right = size - 1
    while left < right:
        value = arr[left] + arr[right]
        if value > k:
            right -= 1
        elif value < k:
            left += 1
        else:
            return [arr[left], arr[right]]
    return None
