class Solution(object):
    def findRepeatedDnaSequences(self, s):
        mydict = defaultdict(int)
        r = 10
        l = 0
        window = deque()
        window.extend(s[l:r])
        while r < len(s)+1:
            mydict[''.join(window)] +=1
            window.popleft()
            if r < len(s):
                window.append(s[r])
            r +=1
            l +=1
        arr = []
        for i in mydict:
            if mydict[i] >1:
                arr.append(i)
        return arr