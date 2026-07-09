class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        m = len(stones)
        while m > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            m -= 2
            if  x < y:
                heapq.heappush_max(stones, y-x)
                m += 1
        

        return stones[0] if m == 1 else 0