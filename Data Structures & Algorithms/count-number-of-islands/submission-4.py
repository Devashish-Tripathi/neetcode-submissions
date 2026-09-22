class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
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
            self.parents[px] = py
            self.rank[py] += 1
        else:
            self.parents[py] = px
            self.rank[px] += 1
        return True
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        Obj = DSU(m*n)
        nbrs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rngx, rngy = range(m), range(n)
        for i in rngx:
            for j in rngy:
                if grid[i][j] == "1":
                    root = i*n + j
                    for dx, dy in nbrs:
                        nx, ny = i + dx, j + dy
                        if nx in rngx and ny in rngy and grid[nx][ny] == "1":
                            Obj.union(root, nx*n+ny)
        roots = set()
        for idx in Obj.parents:
            if grid[idx//n][idx%n] == "1":
                roots.add(Obj.find(idx))

        return len(roots)

        