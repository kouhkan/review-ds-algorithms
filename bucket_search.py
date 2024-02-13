def bucketSort(arr):
    print(arr)

    # Assuming arr only contains 0, 1 or 2
    counts = []
    for _ in range(len(arr)):
        counts.append(0)

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    print(counts)

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr


a = bucketSort([3, 3, 5, 2, 1, 1, 0, 0, 3, 6])
print(a)
