class Solution:
    def scoreOfString(self, s: str) -> int:
        diff = 0
        for i in range(1,len(s)):
            diff += abs(ord(s[i])-ord(s[i-1]))
        return diff