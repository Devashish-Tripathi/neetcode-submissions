class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profs = []
        capitals = [(cap, prof) for cap, prof in zip(capital, profits)]
        heapq.heapify(capitals)
        for _ in range(k):
            while capitals and capitals[0][0] <= w:
                c, p = heapq.heappop(capitals)
                heapq.heappush_max(profs, p)
            if not profs:
                break
            w += heapq.heappop_max(profs)
        return w