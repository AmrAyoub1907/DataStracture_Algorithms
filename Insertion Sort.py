def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        index = i
        while index > 0 and arr[index - 1] > temp:
            arr[index] = arr[index - 1]
            index -= 1

        arr[index] = temp
        
arr = [54,26,93,17,77,31,44,55,20]
insertion_sort(arr)
print arr
