class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n - 1)
        
        value = factorial(n)
        count = 0
        while value % 10 == 0:
            count +=1
            value = value//10
        return count