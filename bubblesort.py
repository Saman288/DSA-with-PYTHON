def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range( n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr= [-2,45,0,11,-9]
print(arr)
bubbleSort(arr)
print(arr)
