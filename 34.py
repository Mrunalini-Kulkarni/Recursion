# Compute the GCD of two numbers using Euclidean Algorithm

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

num1 = int(input("Enter the num1:"))
num2 = int(input("Enter the num2:"))
print(f"GCD of {num1} and {num2} is:", gcd_recursive(num1, num2))
