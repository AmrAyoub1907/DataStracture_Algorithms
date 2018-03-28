def find1DPeak(arr, lo, hi, n):
    mid = (lo + hi)/2
    if((mid == 0 or arr[mid] >= arr[mid-1])
       and(mid == n-1 or arr[mid] >= arr[mid+1])):
        return arr[mid]
    elif(mid > 0 and arr[mid-1] > arr[mid]):
        return find1DPeak(arr, lo , mid - 1, n)
    else:
        return find1DPeak(arr, mid + 1, hi, n)

arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", find1DPeak(arr, 0, n-1, n))