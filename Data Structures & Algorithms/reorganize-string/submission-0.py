class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for ch in s:
            counts[ch] += 1
        maxHeap = [(-ct, ch) for ch, ct in counts.items()]
        heapq.heapify(maxHeap)
        ans = ""
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            ct, char = heapq.heappop(maxHeap)
            ans += char
            ct += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if ct < 0:
                prev = (ct, char)
        return ans