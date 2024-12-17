class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int: 
        c0 = 0
        c1 = 0
        l = 0
        result = 0
        r = 0
        while r < len(s):
            if s[r] == '0':
                c0 += 1
            else:
                c1 += 1
            while c1 > k and c0 > k:
                if s[l] == '0':
                    c0 -= 1
                else:
                    c1 -= 1
                l += 1
            result += r - l + 1
            r +=1
        return result
