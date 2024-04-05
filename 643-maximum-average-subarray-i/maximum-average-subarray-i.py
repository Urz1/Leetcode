class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxim = sum(nums[0:k])
        new  = maxim
        count = k
        for i in range(1,len(nums)):
            if count < len(nums):
                new += nums[count] - nums[i-1]
                maxim = max(maxim,new)
            else:
                break
            count += 1
        return maxim/k
