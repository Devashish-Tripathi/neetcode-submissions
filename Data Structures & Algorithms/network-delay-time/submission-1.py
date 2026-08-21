class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connections = {x: [] for x in range(1, n+1)}
        for source, target, time in times:
            connections[source].append((target, time))
        
        times = {}
        def dfs(node, curr_time):
            if node in times:
                if times[node] <= curr_time:
                    return
            times[node] = curr_time

            for nbr, time in connections[node]:
                dfs(nbr, curr_time + time)
        
        dfs(k, 0)

        if len(times) < n:
            return -1
        return max(times.values()) 
