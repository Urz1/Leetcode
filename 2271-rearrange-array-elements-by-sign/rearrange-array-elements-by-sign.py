class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        arr = []
        for i in range(len(nums)/2):
            arr.append(pos[i])
            arr.append(neg[i])
        return arr