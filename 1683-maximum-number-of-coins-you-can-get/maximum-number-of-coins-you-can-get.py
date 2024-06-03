class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        maxim = 0
        for i in range(-2, -(len(piles)//3) * 2 - 1, -2):
            maxim += piles[i]
        return maxim
       