# Leetcode 1342.Number of Steps to Reduce a Number to Zero using recursion

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        n = num
        while n != 0:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n - 1
            steps += 1
        return steps

solution = Solution()
print(solution.numberOfSteps(14))