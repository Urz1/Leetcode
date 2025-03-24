class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recurse(left,right):
            mid = (right + left)//2
            if nums[mid] == target:
                return mid
            elif left>right:
                return -1
            if nums[mid] > target:
                return recurse(left,mid-1)
            else:
                return recurse(mid+1,right)
        return recurse(0,len(nums)-1)