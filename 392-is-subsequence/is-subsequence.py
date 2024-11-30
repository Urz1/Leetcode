class Solution(object):
    def isSubsequence(self, s, t):
        count = 0
        l = 0
        r = 0
        while r < len(t):
            if l<len(s) and s[l] == t[r]:
                count +=1
                l +=1
            r+=1
        return True if count == len(s) else False 
            
        