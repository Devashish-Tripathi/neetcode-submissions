class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        nbrs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x, y, ocean):
            ocean.add((x, y))
            for dx, dy in nbrs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in ocean and heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, ocean)
        
        # from pacific
        pacific = set()
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)
        
        # from atlantic
        atlantic = set()
        for i in range(m):
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(m-1, j, atlantic)
        
        return list(pacific & atlantic)
