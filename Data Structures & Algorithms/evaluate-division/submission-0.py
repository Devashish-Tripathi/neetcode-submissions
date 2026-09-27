class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q, visit = deque([(src, 1)]), set()
            visit.add(src)

            while q:
                node, wt = q.popleft()
                if node == target:
                    return wt
                for nei, weights in adj[node]:
                    if nei not in visit:
                        q.append((nei, wt*weights))
                        visit.add(nei)
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]