class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        maxim = max(0,max(prefix))
        mini = min(0,min(prefix))
        return abs(mini) + abs(maxim)