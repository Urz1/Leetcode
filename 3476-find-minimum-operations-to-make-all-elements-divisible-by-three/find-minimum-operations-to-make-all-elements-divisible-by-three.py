class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        divide = 0
        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                divide +=1
        return divide