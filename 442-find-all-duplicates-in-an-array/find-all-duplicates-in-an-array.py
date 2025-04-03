class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num = 0
        ans = []
        while num < len(nums):
            pos = nums[num]-1
            if nums[num] == 0:
                num +=1
            elif nums[pos] == nums[num] and pos != num:
                ans.append(nums[num])
                nums[pos] = 0
            elif nums[pos] != nums[num]:
                nums[pos] , nums[num] = nums[num], nums[pos]
            else:
                num +=1
        return ans