class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures = []
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    treasures.append((i, j))
                    visited.add((i, j))

        queue = deque(treasures)
        nbrs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
                x, y = queue.popleft()
                for dx, dy in nbrs:
                    nx, ny = x+dx, y+dy
                    if (nx, ny) in visited: continue
                    if nx < m and nx >= 0 and ny < n and ny >= 0:
                        if grid[nx][ny] != -1 and grid[nx][ny] != 0:
                            grid[nx][ny] = min(grid[nx][ny], grid[x][y]+1)
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                        