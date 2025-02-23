class Solution:
    def maximumGap(self, nums: List[int]) -> int:
       self=0
       l=len(nums)
       if l<2:
        return 0
       list.sort(nums)
       for i in range(1,l):
        if self < nums[i]-nums[i-1]:
            self= nums[i]-nums[i-1]

       return self