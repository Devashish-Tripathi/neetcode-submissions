class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []
        for idx, (eTime, pTime) in enumerate(tasks):
            heapq.heappush(pending, (eTime, pTime, idx))
        
        time = 0
        ans = []
        available = []
        while pending or available:
            while pending and pending[0][0] <= time:
                eTime, pTime, i = heapq.heappop(pending)
                heapq.heappush(available, (pTime, i))
            
            if not available:
                time = pending[0][0]
                continue
            
            pTime, i = heapq.heappop(available)
            time += pTime
            ans.append(i)
        
        return ans