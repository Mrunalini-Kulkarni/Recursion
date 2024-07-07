# For any positive value of N, print 1 to N without using for or while loops via recursion (Reverse Countdown)

def countdown(n,i):
    if i == n+1:
        print ("Done")
    else:
        print (i)
        countdown(n,i+1)
i=0
countdown(5,i)