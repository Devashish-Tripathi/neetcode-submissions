class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_index = []
        fresh_fruits = 0
        num_minutes = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_index.append((i, j))
                elif grid[i][j] == 1:
                    fresh_fruits += 1

        nbrs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while fresh_fruits > 0 and rotten_index:
            for _ in range(len(rotten_index)):
                rf_x, rf_y = rotten_index.pop(0)
                for dx, dy in nbrs:
                    nx, ny = rf_x + dx, rf_y + dy
                    if nx >= 0 and nx < m and ny >=0 and ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        rotten_index.append((nx, ny))
                        fresh_fruits -= 1
            num_minutes += 1

        if fresh_fruits != 0: return -1

        return num_minutes