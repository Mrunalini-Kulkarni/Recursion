# Find maximum and minimum of Array elements using recursion

def findMinRec(A, n):  
	if (n == 1): 
		return A[0] 
	return min(A[n - 1], findMinRec(A, n - 1)) 

def findMaxRec(A, n): 
    if (n == 1): 
        return A[0] 
    return max(A[n - 1], findMaxRec(A, n - 1)) 


if __name__ == '__main__': 
	A = [1, 4, 45, 6, -50, 10, 2] 
	n = len(A) 
	print(findMinRec(A, n)) 
	print(findMaxRec(A, n)) 

 
