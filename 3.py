# Given two numbers x and y find the product using recursion

def product( x , y ): 
	if x < y: 
		return product(y, x) 
	elif y != 0: 
		return (x + product(x, y - 1)) 
	else: 
		return 0 
x = int(input())
y = int(input())
print( product(x, y)) 
