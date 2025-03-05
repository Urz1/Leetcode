class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = {}  
        for i in range(len(nums2)):  
            index[nums2[i]] = i   
        
        ans = []  
        
        for i in range(len(nums1)):  
            ind = index[nums1[i]]   
            left = ind   
            
            while left < len(nums2) - 1 and nums2[left] <= nums2[ind]:  
                left += 1  
            if left < len(nums2) and nums2[left] > nums2[ind]:  
                ans.append(nums2[left])  
            else:  
                ans.append(-1)  
        
        return ans
