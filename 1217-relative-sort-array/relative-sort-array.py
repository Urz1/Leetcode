class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        count = Counter(arr1)
        pos = 0 
        arr = []
        for i in arr2:
            for j in arr1:
                if i == j:
                    arr.append(i)
        
        difference = [item for item in arr1 if item not in arr]
        arr.extend(sorted(difference))
        return(arr)
        