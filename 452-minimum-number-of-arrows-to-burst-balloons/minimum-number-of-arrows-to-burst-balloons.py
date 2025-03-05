class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 1
        ar = points[0][1]
        for i in range(1,len(points)):
            if points[i][0]<= ar <= points[i][1]:
                continue 
            else:
                ar = points[i][1]
                count +=1
        return count