# Convert decimal to binary using recursion

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

digit = int(input())

convertToBinary(digit)
print()
