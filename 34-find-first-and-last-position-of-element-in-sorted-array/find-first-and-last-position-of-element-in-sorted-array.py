class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        idx = float("inf")
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                idx = mid
                break
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if idx==float("inf"):
            return [-1,-1]
        low = idx 
        high = idx 
        while nums[low]==nums[mid] and low>0 and nums[low-1]==nums[mid]:
            low-=1
        while nums[high]==nums[mid] and high<len(nums)-1 and nums[high+1]==nums[mid]:
            high+=1
        return [low,high]
