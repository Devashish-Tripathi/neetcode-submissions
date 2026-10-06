class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        pqueue = [(-ct, ch) for ct, ch in [(a, 'a'), (b, 'b'), (c, 'c')] if ct > 0]
        heapq.heapify(pqueue)
        while pqueue:
            ct, ch = heapq.heappop(pqueue)
            if len(ans) >= 2 and ans[-1] == ans[-2] == ch:
                if not pqueue:
                    break
                ct2, ch2 = heapq.heappop(pqueue)
                ans += ch2
                ct2 += 1
                if ct2 < 0:
                    heapq.heappush(pqueue, (ct2, ch2))
                heapq.heappush(pqueue, (ct, ch))
            else:
                ans += ch
                ct += 1
                if ct < 0:
                    heapq.heappush(pqueue, (ct, ch)) 
        return ans