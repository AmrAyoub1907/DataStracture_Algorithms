def countingSort(arr, exp):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * n

    # initialize count array as 0
    count = [0] * 10

    for i in range(0, n):
        index = (arr[i] / exp)
        count[index % 10] += 1

        # Change count[i] so that count[i] now contains actual
        #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    #arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    maximaum = max(arr)  # get maximum number of digits
    exp = 1
    while maximaum / exp > 0:
        countingSort(arr, exp)
        exp *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i]),
