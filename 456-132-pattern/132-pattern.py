class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # decreasing monotonic stack
        stack = []
        popped = -float('inf')
        nums.reverse()
        for num in nums:
            if num < popped:
                return True
            while stack and stack[-1] < num:
                popped = stack.pop()
            stack.append(num)
            
        return False

