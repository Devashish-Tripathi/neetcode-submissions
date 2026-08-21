class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [1] * (n)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        rx, ry = self.rank[px], self.rank[py]
        if rx < ry:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        else:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        return True        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            p1_x, p1_y = points[i]
            for j in range(i+1, n):
                p2_x, p2_y = points[j]
                distance = abs(p2_x-p1_x) + abs(p2_y-p1_y)
                edges.append((distance, i, j))
        
        edges.sort()
        ans = 0
        UF = UnionFind(n)
        for dist, i, j in edges:
            if UF.union(i, j):
                ans += dist
        return ans
