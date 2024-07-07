# Find the value of 'a' raised to the power 'b' using recursion

def power(a,b):
    if b ==0:
        return 1
    elif b<0:
        return 1/power(a,-b)
    else:
        return  a*power(a,b-1)
a = int(input())
b = int(input())
print(power(a,b))