class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # pls check this out later 
        merged = sorted(nums1 + nums2)   
        n = len(merged)
        mid = n // 2
        if n % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0  
        else:
            return merged[mid]