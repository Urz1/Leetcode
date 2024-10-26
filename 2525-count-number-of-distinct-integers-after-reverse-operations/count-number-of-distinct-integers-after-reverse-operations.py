class Solution(object):
    def countDistinctIntegers(self, nums):
        mset = set(nums)
        for i in range(len(nums)):
            reversed_num = int(str(nums[i])[::-1])
            mset.add(reversed_num)
        return len(mset)
        