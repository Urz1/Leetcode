class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_c = []
        max_r = []
        for col in range(len(grid)):
            r = 0
            c = 0
            for row in range(len(grid)):   
                r = max(grid[row][col],r)
                c = max(grid[col][row],c)
                
            max_c.append(c)
            max_r.append(r)
        _sum = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                _sum += min(max_c[col], max_r[row]) - grid[row][col]
        return _sum