class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        prefix = [0] *(len(nums) + 1)
        for query in queries:
            prefix[query[0]] -= 1
            prefix[query[1]+1] += 1
        prefix = list(accumulate(prefix))
        for a, b in zip(prefix,nums):
            if a + b > 0 :
                return False
        return True
     