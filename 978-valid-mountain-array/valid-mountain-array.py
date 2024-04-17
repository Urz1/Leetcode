class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag = True
        larg = max(arr)
        for i in range(len(arr)):
            if arr[i] == larg:
                idx = i
        if idx == 0 or idx == len(arr)-1:
            return False
        for i in range(1,len(arr)):
            if i<= idx and arr[i]<=arr[i-1]:
                return False
            elif i > idx and arr[i] >= arr[i-1]:
                return False
        return True

