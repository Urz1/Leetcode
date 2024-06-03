class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        count = 0
        compare = 0 
        for i in costs:
            compare +=i
            if compare<=coins:
                count+=1
            else:
                break
        return count