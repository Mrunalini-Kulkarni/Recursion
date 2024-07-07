# For any positive value of N, print N to 1 without using for or while loops via recursion (Countdown)

def countdown(n):
    if n <=0:
        print("Booom")
    else:
        print(n)
        countdown(n-1)
countdown(10)