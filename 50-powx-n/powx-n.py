class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return x**0
        def recur(x,n):
            if n == 1:
                return x
            if n == -1:
                return 1/x
            if n % 2 == 0:
                power = recur(x, n//2)
                return power**2
            power = recur(x, n//2)
            return x * power**2 
        return recur(x,n)