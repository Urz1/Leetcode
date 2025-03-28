class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # check for confidence
        position.sort()
        def canbe_placed(index):
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= index:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        low = 1
        high = position[-1] - position[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if canbe_placed(mid):
                ans = mid
                low = mid +1
            else:
                high = mid -1
        return ans
