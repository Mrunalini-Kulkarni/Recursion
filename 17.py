# Leetcode 509.Find the nth number in a Fibonacci Series using Recursion

class Solution:
    def fib(self, n: int) -> int:
        fib_series = [0, 1]
        if n == 0: 
            return 0
        else:
            while len(fib_series) <=n :
                next_fib = fib_series[-1] + fib_series[-2]
                fib_series.append(next_fib)
            return fib_series[-1]