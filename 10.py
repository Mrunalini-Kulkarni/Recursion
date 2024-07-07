# Reverse a string uing recursion

def palindrome(str):
    str = str.lower()
    if len(str)==0:
        return str
    else:
        return palindrome(str[1:])+str[0]
    
str="Hello"
if (palindrome(str)==str.lower()):
    print("String ",str,"is palindrome and it's palindrome is")
else:
    print("String ",str,"is not palindrome")