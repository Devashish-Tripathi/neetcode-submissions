class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ls = []
        heapq.heapify(ls)
        len_heap = 0
        for elem in nums:
            heapq.heappush(ls, elem)
            if len_heap < k:
                len_heap += 1
            else:
                heapq.heappop(ls)
        return heapq.heappop(ls)