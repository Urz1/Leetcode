class Solution(object):
    def addSpaces(self, s, spaces):
        l = 0
        arr = []
        for r in range(len(s)):
            if l<len(spaces) and r == spaces[l]:
                arr.append(" ")
                l+=1
            arr.append(s[r])
        return ''.join(arr)