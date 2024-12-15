class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        arr = []
        for i in count:
            if count[i] > len(nums)//3:
                arr.append(i)
        return arr