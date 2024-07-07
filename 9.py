# Find length of string recursion

def recursive_length(the_string):
    if the_string == '':
        return 0
    return 1 + recursive_length(the_string[1:])

my_string = "Design & Ananlysis of Algorithm"
length = recursive_length(my_string)
print(f"Length of the string: {length}")