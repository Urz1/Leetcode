class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def traverse(row, col):
            nonlocal perimeter
            count = 0
            for dr, dc in directions:
                n_r = dr + row
                n_c = dc + col
                if inbound(n_r, n_c) and grid[n_r][n_c] == 1:
                    count += 1
                    if (n_r, n_c) not in visited:
                        visited.add((n_r, n_c))
                        traverse(n_r, n_c)
            perimeter += (4 - count)

        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    traverse(i, j)
                    found = True
                    break
            if found:
                break

        return perimeter
                