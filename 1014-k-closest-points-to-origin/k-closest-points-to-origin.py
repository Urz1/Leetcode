class Solution(object):
    def kClosest(self, points, k):
        arr = []
        for i in range(len(points)):
            arr.append([points[i][0]**2 + points[i][1]**2,i])
        arr.sort()
        arr2 = []
        for i in range(k):
            arr2.append(points[arr[i][1]])
        return arr2