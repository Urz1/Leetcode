class Solution(object):
    def checkInclusion(self, s1, s2):
        checker = Counter(s1)
        l = 0
        r = len(s1)
        comp = Counter(s2[:r])
        while r < len(s2):
            if comp == checker:
                return True
            comp[s2[l]] -=1
            if comp[s2[l]] == 0:
                del comp [s2[l]]
            comp[s2[r]] = comp.get(s2[r],0) +1
            l +=1
            r+=1
            
        return comp == checker

        