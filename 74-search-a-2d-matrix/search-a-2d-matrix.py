class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def check(index):
            low, high = 0, len(matrix[index]) - 1   
            while low <= high:
                mid = (low + high) // 2
                if matrix[index][mid] == target:
                    return True
                elif matrix[index][mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False

        low, high = 0, len(matrix) - 1   
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:   
                return check(mid)
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
