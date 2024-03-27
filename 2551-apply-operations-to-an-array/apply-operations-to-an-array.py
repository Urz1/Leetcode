class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        clone = [0]*len(nums)
        index = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                clone[index] = nums[i]
                index +=1
        return clone