class Solution(object):
    def isSubsequence(self, s, t):
        l, r = 0, 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            r += 1
        return l == len(s)

    def findLUSlength(self, strs):
        strs.sort(key=len, reverse=True)  
        for i, s in enumerate(strs):
            is_uncommon = True
            for j, t in enumerate(strs):
                if i != j and self.isSubsequence(s, t):
                    is_uncommon = False
                    break
            if is_uncommon:
                return len(s)
        return -1

        
    # def isSubsequence(self, s, t):
    #     count = 0
    #     l = 0
    #     r = 0
    #     while r < len(t):
    #         if l<len(s) and s[l] == t[r]:
    #             count +=1
    #             l +=1
    #         r+=1
    #     return True if count == len(s) else False
    # def findLUSlength(self, strs):
    #     strs.sort()
    #     mydict = Counter(strs)
    #     l = 0
    #     for r in range(1,len(strs)):
    #         if self.isSubsequence(strs[l],strs[r]) :
    #             del mydict[strs[l]]    
    #             l +=1
    #         elif self.isSubsequence(strs[r],strs[l]):
    #             del mydict[strs[r]] 
    #         while not (self.isSubsequence(strs[l],strs[r])) and l < r: 
    #             l +=1   
    #     size = -1
    #     for key in mydict:
    #         size = max(size,len(key))
    #     return size
        



