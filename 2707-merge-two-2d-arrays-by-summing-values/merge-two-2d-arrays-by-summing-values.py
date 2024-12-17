class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        arr = []
        l1 = 0
        l2 = 0
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1][0] == nums2[l2][0]:
                arr.append([nums1[l1][0],nums1[l1][1] + nums2[l2][1]])
                l1 += 1
                l2 += 1
            elif nums1[l1][0] < nums2[l2][0]:
                arr.append(nums1[l1])
                l1 += 1
            else:
                arr.append(nums2[l2])
                l2 += 1
        arr.extend(nums1[l1:])
        arr.extend(nums2[l2:])
        return arr