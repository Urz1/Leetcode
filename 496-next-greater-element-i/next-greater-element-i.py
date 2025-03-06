class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        tracker = defaultdict(int)
        for i in nums2:
            tracker[i] = -1
        for num in nums2:
            while stack and stack[-1] < num:
                tracker[stack.pop()] = num
            stack.append(num)
        return [tracker[val] for val in nums1]