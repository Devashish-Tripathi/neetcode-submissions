class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {x:[] for x in range(n)}
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        
        queue = [(0, 0, src)] # cost to get there, n_stops to get there, airport number
        at_dest = False
        
        while queue:
            curr_cost, curr_stops, curr_airp = heapq.heappop(queue)
            if curr_airp == dst:
                return curr_cost
            nbrs = graph[curr_airp]
            for airp, cost in nbrs:
                if airp == dst or (airp != dst and curr_stops + 1 <= k):
                    # if we can reach some unvisited by a better way?
                    # what about those visited already?
                    heapq.heappush(queue, (curr_cost+cost, curr_stops+1, airp))
        
        return -1