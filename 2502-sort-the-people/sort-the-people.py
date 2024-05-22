class Solution(object):
    def sortPeople(self, names, heights):
        for i in range(len(heights)):
            for j in range(1,len(heights)):
                if heights[j-1]<heights[j]:
                    heights[j-1],heights[j] = heights[j],heights[j-1]
                    names[j-1],names[j] = names[j],names[j-1]
        return names