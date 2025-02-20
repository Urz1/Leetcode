class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] + list(accumulate(nums))

        for i in range(1,len(nums)+1):
            if prefix[i-1] == prefix[-1] - prefix[i]:
                return i - 1
        return -1