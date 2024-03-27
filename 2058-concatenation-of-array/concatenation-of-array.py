class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ar = nums
        ar.extend(nums)
        return ar