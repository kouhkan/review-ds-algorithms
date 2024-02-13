def binary_search(arr, t):
    l = 0
    r = len(arr) - 1

    mid = (l + r) // 2
    while l <= r:
        if t > arr[mid]:
            l = mid + 1
        elif t < arr[mid]:
            r = mid - 1
        else:
            return mid

    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))