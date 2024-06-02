class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort()
        wide = 0
        for i in range(1,len(points)):
            wide = max(wide,points[i][0]- points[i-1][0])
        return wide
        