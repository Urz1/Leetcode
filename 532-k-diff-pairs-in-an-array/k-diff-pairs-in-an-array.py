class Solution(object):
    def findPairs(self, nums, k):
        nums.sort()
        l = 0
        count = 0
        check = set()

        for r in range(1,len(nums)):
            while nums[r] -nums[l] > k and l<r:
                l+=1
            if r>l and nums[r] - nums[l] == k and (nums[l],nums[r]) not in check:
                count +=1
                check.add((nums[l],nums[r]))
            
        return count

        