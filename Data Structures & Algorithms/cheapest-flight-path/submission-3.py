class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {x:[] for x in range(n)}
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        
        queue = [(0, 0, src)] # cost to get there, n_stops to get there, airport number
        at_dest = False
        visited_stops = [float("inf")] * n

        while queue:
            curr_cost, curr_stops, curr_airp = heapq.heappop(queue)
            if curr_airp == dst:
                return curr_cost
            # had a better path already
            if curr_stops >= visited_stops[curr_airp] or curr_stops > k:
                continue
            visited_stops[curr_airp] = curr_stops

            nbrs = graph[curr_airp]
            for airp, cost in nbrs:
                heapq.heappush(queue, (curr_cost+cost, curr_stops+1, airp))
        
        return -1