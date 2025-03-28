class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isZeroArray(index):
            prefix = [0] *(len(nums) + 1)
            for i in range(index):
                prefix[queries[i][0]] -= queries[i][2]
                prefix[queries[i][1]+1] += queries[i][2]
            prefix = list(accumulate(prefix))
            for a, b in zip(prefix,nums):
                if a + b > 0 :
                    return False
            return True
        low = 0
        high = len(queries)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if isZeroArray(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans