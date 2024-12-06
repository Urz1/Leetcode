class Solution(object):
    def maxCount(self, banned, n, maxSum):
        ban = Counter(banned)
        count = 0
        rsum = 0
        for i in range(1,n+1):
            if i not in ban:
                rsum += i
                if rsum <= maxSum:
                    count +=1
        return count