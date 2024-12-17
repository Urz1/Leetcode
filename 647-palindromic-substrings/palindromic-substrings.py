class Solution:
    def countSubstrings(self, s: str) -> int:
        pal = 0

        for i in range(len(s)):
            l,r= i,i
            while l >= 0 and r < len(s)and s[l] == s[r]:
                l -= 1
                r += 1
                pal += 1
            l,r = i , i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                pal += 1
        return pal