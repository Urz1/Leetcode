class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        previous = self.getRow(rowIndex-1)
        curr = [1]
        for i in range(len(previous)-1):
            curr.append(previous[i]+previous[i+1])
        curr.append(1)
        return curr