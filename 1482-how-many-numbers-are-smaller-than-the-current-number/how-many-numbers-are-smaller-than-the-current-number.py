class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        counter = {}
        arr = sorted(nums)
        arr2 = []
        for i in range(len(arr)):
            if arr[i] not in counter:
                counter[arr[i]] = i
        for i in nums:
            arr2.append(counter[i])
        return arr2
        
                