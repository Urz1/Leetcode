class Solution(object):
    def findLUSlength(self, a, b):
        mydict = {a:a}
        if b in mydict:
            return -1
        return max(len(a),len(b))
        