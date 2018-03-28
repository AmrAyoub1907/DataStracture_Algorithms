def binary_insertion_sort(arr,val):
    lo = 0
    hi = len(arr)-1
    while lo < hi :
        med = (lo+hi)/2
        if val > arr[med]:
            lo = med+1
        elif val < arr[med]:
            hi = med-1
    return lo
arr = [10 ,15 ,20 ,25 ,30 ,35 ,44 ,55 ]
num = 16
index = binary_insertion_sort(arr, num)
arr.insert(index, num)
print arr