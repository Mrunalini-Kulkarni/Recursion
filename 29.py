# Perform Insertion Sort using Recursion

def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last

arr = [14, 15, 95, 20, 74, 54, 69, 85]
n = len(arr)
insertion_sort_recursive(arr, n)

print("Sorted array:", arr)
