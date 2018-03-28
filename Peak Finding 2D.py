def find2DPeak(arr, rows , cols,midcol):
    arrMax = -1
    arrMaxind= -1
    for i in range(0, rows):
        if(arr[midcol][i]>arrMax):
            arrMax =arr[midcol][i]
            arrMaxind = i

    Max = arr[midcol][arrMaxind]
    if (midcol == 0 or midcol == cols - 1):
        return Max
    elif(arr[midcol-1][arrMaxind]<=Max and arr[midcol+1][arrMaxind]<=Max):
        return Max
    elif(Max < arr[midcol-1][arrMaxind]):
        return find2DPeak(arr,rows,cols,midcol/2)
    elif(Max < arr[midcol+1][arrMaxind]):
        return find2DPeak(arr,rows,cols,midcol + midcol/2)

arr = [[10, 8, 10, 10],[14, 13, 12, 11 ],[15, 9, 11, 21 ],[16, 17, 19, 20 ]]
rows = 4
cols=4
print("Index of a peak point is", find2DPeak(arr, rows, cols,cols/2))