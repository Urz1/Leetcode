class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxim = 0
        for i in range(2,len(nums)):
            if nums[i-1] + nums[i-2] > nums[i]:
                maxim = max(maxim,nums[i-1] + nums[i-2] + nums[i])
        return maxim if maxim > 0 else 0
        