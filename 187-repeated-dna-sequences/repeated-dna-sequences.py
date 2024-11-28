class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10:
            return []
        mydict = defaultdict(int)
        r = 10
        l = 0
        while r < len(s)+1:
            window = s[l:r]
            mydict[window] +=1
            r +=1
            l +=1
        arr = []
        for i in mydict:
            if mydict[i] >1:
                arr.append(i)
        return arr