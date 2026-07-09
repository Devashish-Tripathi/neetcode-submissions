class UnionFind:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        rx, ry = self.rank[px], self.rank[py]
        if rx < ry:
            px, py = py, px
        self.parents[py] = px
        self.rank[px] += 1

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def convert_to1d(x, y, n):
            return n*x + y
        def convert_to2d(idx, m, n):
            x = idx//n
            y =  idx - x*n  
            return x, y

        ufind = UnionFind(m*n)
        nbrs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        xrange, yrange = range(m), range(n)
        for x in range(m):
            for y in range(n):
                idx_parent = convert_to1d(x, y, n)
                value = grid[x][y]
                for dx, dy in nbrs:
                    nx, ny = x+dx, y+dy
                    if nx in xrange and ny in yrange and grid[nx][ny] == value:
                        idx_child = convert_to1d(nx, ny, n)
                        ufind.union(idx_parent, idx_child)
        # print(m, n)
        for i in range(m*n):
            ufind.find(i)
        # print(collections.Counter(ufind.parents).most_common())
        for idx_parent, area in collections.Counter(ufind.parents).most_common():
            x, y = convert_to2d(idx_parent, m, n)
            if grid[x][y] == 1:
                return area
        return 0

        