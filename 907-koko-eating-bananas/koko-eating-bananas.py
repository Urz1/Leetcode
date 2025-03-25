class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(cap):
            hour = 0
            for pile in piles:
                if cap > pile:
                    hour +=1
                else:
                    hour += ceil(pile/cap)
            return hour <= h
        low = ceil(sum(piles)/h)
        high = max(piles)
        ans = None
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans
