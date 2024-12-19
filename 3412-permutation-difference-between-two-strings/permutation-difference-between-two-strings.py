class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        scount = {s[i]:i for i in range(len(s))}
        tcount = {t[i]:i for i in range(len(t))}
        diff = 0
        for i in s:
            diff += abs(scount[i] - tcount[i])
        return diff