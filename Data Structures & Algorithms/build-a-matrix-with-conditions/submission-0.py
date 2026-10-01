class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, visit, path, order):
            # this is here first to detect cycle
            if src in path:
                return False
            # this is here for efficiency, if same node can be reached from two paths
            # then encountering it again means that there is no cycle so no need to run
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True        
        
        def topo_sort(edges):
            adj = defaultdict(list)
            for src, dst in edges:
                # append all the possible "destinations" from an edge
                adj[src].append(dst)
            
            visit, path = set(), set()
            order = []
            # if cycle detected, basically if 1 is below 2 is below 3 is below 1, not possible
            # return back
            # else the order of placing is the order in which the values are encountered
            # for example 2 is above 1 and 1 is above 3 are two conditions
            # we iterate from 1, do dfs on 1, go to 3, do dfs on 3, find nothing wrong
            # we append 3, we go back, we append 1, we go back, go to dfs on 2, go to 1, already visited
            # go back, append 2, so order is [3, 1, 2] BUT this is the reverse of what we need, so rev it
            # and send [2, 1, 3], satisfying the answer
            for src in range(1, k+1):
                if src not in visit:
                    if not dfs(src, adj, visit, path, order):
                        return []
            return order[::-1]

        
        rowOrder = topo_sort(rowConditions)
        if not rowOrder: return []
        colOrder = topo_sort(colConditions)
        if not colOrder: return []

        val_to_row = {num:i for i, num in enumerate(rowOrder)}
        val_to_col = {num:i for i, num in enumerate(colOrder)}
        res = [[0]*k for _ in range(k)]
        for num in range(1, k+1):
            res[val_to_row[num]][val_to_col[num]] = num
        return res