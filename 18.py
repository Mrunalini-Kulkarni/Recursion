# Geekonacci Number

def find(A, B, C, N):
	if N == 1:
		return A
	elif N == 2:
		return B
	elif N == 3:
		return C

	return find(A, B, C, N - 1) + find(A, B, C, N - 2) + find(A, B, C, N - 3)

A = 1
B = 3
C = 2
N = 4

result = find(A, B, C, N)
print(result)

