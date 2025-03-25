class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(cap):
            day = 1
            capacity = 0

            for weight in weights:
                if weight + capacity <= cap:
                    capacity += weight
                else:
                    capacity = weight
                    day += 1
            return day <= days

        low = max(weights)
        high = sum(weights)
        ans = None
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
