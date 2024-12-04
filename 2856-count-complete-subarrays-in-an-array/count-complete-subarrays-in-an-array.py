class Solution(object):
    def countCompleteSubarrays(self, nums):
        size = len(set(nums))
        count = 0
        subarray = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            subarray[nums[r]] +=1
            while len(subarray) >= size:
                count += len(nums) - r
                subarray[nums[l]] -= 1  
                if subarray[nums[l]] == 0:  
                    del subarray[nums[l]]
                l += 1
        return count
            



