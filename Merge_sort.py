def merge(arr, l, m, r):
    left = arr[l:(m + 1)]
    right = arr[(m + 1):(r + 1)]

    i = 0
    j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    if j < len(right):
        arr[k:len(right)-1] = right[j:len(right)-1]


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) / 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(arr, 0, len(arr) - 1)
print arr
