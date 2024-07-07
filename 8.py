# Reverse a number using recursion

def reverse(n,r):
    if n==0:
        return r
    else:
        return reverse(n//10,r*10 + n%10)
print(reverse(7894,0))