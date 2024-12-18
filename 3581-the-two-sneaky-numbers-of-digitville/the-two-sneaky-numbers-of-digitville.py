class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                arr.append(nums[i])
        return arr