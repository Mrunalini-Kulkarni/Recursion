# Perform Bubble Sort using Recursion

def bubble_sort_recursive(arr, n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort_recursive(arr, n - 1)

arr = [14, 15, 95, 20, 74, 54, 69, 85]
n = len(arr)
bubble_sort_recursive(arr, n)

print("Sorted array:", arr)
