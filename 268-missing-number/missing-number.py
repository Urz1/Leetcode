class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums_len = len(nums)
        while nums_len > -1:
            if (nums_len in nums):
                pass
            else:
                return nums_len
            nums_len -= 1
        return 