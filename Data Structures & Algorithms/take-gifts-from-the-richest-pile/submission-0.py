import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        ans = 0
        for _ in range(k): 
            best = heapq.heappop(gifts)
            # print(gifts)
            heapq.heappush(gifts, -math.floor(math.sqrt(-best)))
            # print(gifts)
        return -sum(gifts)