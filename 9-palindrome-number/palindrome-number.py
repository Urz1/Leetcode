class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(str(x))
        return y == y[::-1]