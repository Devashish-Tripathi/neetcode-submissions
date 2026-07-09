class UnionFind:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x1, x2):
        p1, p2 = self.parents[x1], self.parents[x2]
        if p1 == p2:
            return
        elif self.rank[p1] >= self.rank[p2]:
            self.parents[p2] = p1
            self.rank[p1] += 1
        else:
            self.parents[p1] = p2
            self.rank[p2] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])

        connected_roots = set()
        for i in range(n):
            connected_roots.add(uf.find(i))
        
        return len(connected_roots)