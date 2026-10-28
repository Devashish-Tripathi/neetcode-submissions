class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        def bfs():
            queue = [(1, 0, 0)]
            visited = set()
            nbrs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            while queue:
                plen, x, y = heapq.heappop(queue)
                visited.add((x, y))
                if x == y == n-1:
                    return plen
                for dx, dy in nbrs:
                    nx, ny = x+dx, y+dy
                    if (nx, ny) not in visited and 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        heapq.heappush(queue, (plen+1, nx, ny))
            return -1
        
        return bfs()