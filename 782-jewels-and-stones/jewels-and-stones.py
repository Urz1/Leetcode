class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        precious = set(jewels)
        count = 0 
        for i in stones:
            if i in precious:
                count +=1
        return count