class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        pa, pb = self.find(x), self.find(y)
        if pa == pb:
            return
        elif self.rank[pa] >= self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += 1
        else:
            self.parent[pa] = pb
            self.rank[pb] += 1

class Solution:

    def getPos(self, i, j, m, n):
        return n*i+j

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n)
        places = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0": continue
                for p in places:
                    nbr_x, nbr_y = i+p[0], j+p[1]
                    if nbr_x >= 0 and nbr_x < m and nbr_y >= 0 and nbr_y < n and grid[nbr_x][nbr_y]=="1":
                        # print(i, j)
                        # print(nbr_x, nbr_y)
                        # print(self.getPos(i, j, m, n), self.getPos(nbr_x, nbr_y, m, n))
                        uf.union(self.getPos(i, j, m, n), self.getPos(nbr_x, nbr_y, m, n))
                        # print(uf.parent)

        islandIdx = set()
        for idx in uf.parent:
            if grid[idx//n][idx%n] == "1":
                islandIdx.add(uf.find(idx))
        
        return len(islandIdx)

        