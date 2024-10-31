class Solution(object):
    def removeElement(self, nums, val):
        pt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
        pos = 0
        for i in range(len(nums)):
            if nums[i] != '_' :
                nums[i],nums[pos] = nums[pos],nums[i]
                pos+=1
        return pos
        