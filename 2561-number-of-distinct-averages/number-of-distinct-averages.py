class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        count = defaultdict(int)
        nums.sort()
        right = len(nums) - 1
        left = 0
        while left < right:
            count[(nums[left]+nums[right])/2] += 1
            left += 1
            right -= 1
        return len(count)