class Solution(object):
    def maxArea(self, height):
        maxim = 0
        i = 0
        n = len(height) - 1
        
        while i < n:
            maxim = max(maxim, (n - i) * min(height[i], height[n]))
            if height[i] < height[n]:
                i += 1
            else:
                n -= 1
        
        return maxim