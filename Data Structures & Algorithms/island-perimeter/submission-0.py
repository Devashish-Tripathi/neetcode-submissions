class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # top
                    if i-1 < 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    # bottom
                    if i+1 == m or grid[i+1][j] == 0:
                        perimeter += 1
                    # left
                    if j-1 < 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    # right
                    if j+1 == n or grid[i][j+1] == 0:
                        perimeter += 1
        return perimeter             
