class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n-1:
            return False
        
        def dfs(node, parent, edge_dct, visited):
            if node in visited:
                return False
            visited.add(node)
            for nbr in edge_dct[node]:
                if nbr == parent:
                    continue
                if not dfs(nbr, node, edge_dct, visited):
                    return False
            return True
        
        edge_dct = {x:[] for x in range(n)}
        for edge in edges:
            edge_dct[edge[0]].append(edge[1])
            edge_dct[edge[1]].append(edge[0])
        visited = set()
        return dfs(0, -1, edge_dct, visited) and len(visited) == n
        