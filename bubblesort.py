def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n - i - 1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Create an unsorted list
my_list = [64, 34, 25, 12, 22, 11, 90]

# Display the unsorted list
print("Unsorted List:")
print(my_list)

# Sort the list using bubble sort
bubble_sort(my_list)

# Display the sorted list
print("\nSorted List:")
print(my_list)
