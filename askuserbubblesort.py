def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range( n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   arr.append(l)
print(arr)
bubbleSort(arr)
print(arr)

