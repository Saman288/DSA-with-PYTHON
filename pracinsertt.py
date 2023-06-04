def insertionSort(array):

    for step in range(1,len(array)):
        key=array[step]
        j= step - 1

        while j>=0 and key < array[j+1]:
            array[j + 1]= array[j]
            j= j -1

        array[j + 1]=key

data=[56,43,12,87,9,5]
insertionSort(data)
print('Data in ascending order:')
print(data)
