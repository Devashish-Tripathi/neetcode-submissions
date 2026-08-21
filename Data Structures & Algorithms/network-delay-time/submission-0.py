class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connections = {x: [] for x in range(1, n+1)}
        for source, target, time in times:
            connections[source].append((target, time))
        
        times = {node: float("inf") for node in range(1, n+1)}
        def dfs(node, time):
            if times[node] <= time:
                return
            times[node] = time
            for nbr, ntime in connections[node]:
                dfs(nbr, time+ntime)
        
        dfs(k, 0)
        ans = max(times.values())
        return ans if ans < float('inf') else -1 