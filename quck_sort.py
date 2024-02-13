def quick_sort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]

            left += 1

    arr[e] = arr[left]
    arr[left] = pivot

    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1, e)

    return arr


arr = [2, 4, 2, 1, 3, 4, 0, 9]
print(quick_sort(arr, 0, len(arr) - 1))
