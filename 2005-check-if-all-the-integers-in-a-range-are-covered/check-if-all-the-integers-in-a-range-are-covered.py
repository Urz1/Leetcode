class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sett = set(num for start, end in ranges for num in range(start, end + 1))
        if left not in sett or right not in sett:
            return False
        else:
            for i in range(left,right):
                if i not in sett:
                    return False
        return True
