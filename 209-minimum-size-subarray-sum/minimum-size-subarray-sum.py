class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        r = 0 
        count = float('inf')
        size = 0
        while r < len(nums):
            size += nums[r]
            while size >= target:
                count = min(count,r - l +1)
                size -= nums[l]
                l+=1
            r+=1
        return 0 if count == float('inf') else count


                