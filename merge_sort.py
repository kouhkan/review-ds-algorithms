def merge(arr, s, m, e):
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i, j = 0, 0
    k = s

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


def merge_sort(arr, s, e):
    if (e - s + 1) <= 1:
        return arr

    mid = (s + e) // 2
    merge_sort(arr, s, mid)
    merge_sort(arr, mid + 1, e)
    merge(arr, s, mid, e)

    return arr


arr = [2, 1, 3, 4, 5, 7]
print(merge_sort(arr, 0, len(arr)))

