class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        count = 0
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                count += len(nums)-i
        return count
       