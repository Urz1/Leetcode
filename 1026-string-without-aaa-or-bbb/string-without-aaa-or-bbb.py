class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a >= 2*b:
            return 'aab'* b + 'a'* (a-2*b)
        elif a >= b:
            return 'aab' * (a-b) + 'ab' * (2*b - a)
        elif b >= 2*a:
            return 'bba' * a + 'b' *(b-2*a)
        else:
            return 'bba' * (b-a) + 'ab' * (2*a - b)