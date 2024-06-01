class Solution(object):
    def sortColors(self, nums):
        count = Counter(nums)
        pos = 0
        if 0 in count:
            nums[pos:pos + count[0]] = [0] * count[0]
            pos += count[0]
        if 1 in count:
            nums[pos:pos + count[1]] = [1] * count[1]
            pos += count[1]
        if 2 in count:
            nums[pos:pos + count[2]] = [2] * count[2]
            pos += count[2]
        