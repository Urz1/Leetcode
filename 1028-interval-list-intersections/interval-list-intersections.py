class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        arr = []
        i, j = 0, 0
        
        while i < len(firstList) and j < len(secondList):
            # Find the start and end of the intersection
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            # Check if there is an intersection
            if start <= end:
                arr.append([start, end])
            
            # Move to the next interval in the list that ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return arr
