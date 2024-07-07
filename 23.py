# Find mean of Array elements using recursion

def findMean(A, N): 
	if (N == 1): 
		return A[N - 1] 
	else: 
		return ((findMean(A, N - 1) *
				(N - 1) + A[N - 1]) / N) 

Mean = 0
A = [6, 7, 8, 9, 10] 
N = len(A) 
print(findMean(A, N)) 

