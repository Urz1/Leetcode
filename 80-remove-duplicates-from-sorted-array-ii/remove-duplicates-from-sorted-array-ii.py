class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        pt = 0
        for i in range(1,len(nums)):
            if nums[pt] == nums[i] and abs(pt - i) >= 2:
                nums[i] = '_'
            elif nums[pt] != nums[i]:
                pt = i
        count = 0
        pos = 0
        for i in range(len(nums)):
            if nums[i] != '_' :
                nums[i],nums[pos] = nums[pos],nums[i]
                pos+=1
        for i in range(len(nums)):
            if nums[i] == '_':
                break
            count +=1
        return (count)
            