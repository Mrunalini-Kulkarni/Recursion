# Find sum of Array elements using recursion

def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


arr = [12, 13, 14, 15]
print(sum(arr))

