class Solution(object):
    def intersect(self, nums1, nums2):
        count1= Counter(nums1)
        count2 = Counter(nums2)
        arr = []
        for i in count1:
            if i in count2:
                arr.extend([i]*min(count1[i],count2[i]))
        return arr