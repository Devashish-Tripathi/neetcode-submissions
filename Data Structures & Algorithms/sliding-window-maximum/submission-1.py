class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        m = len(nums)
        for i in range(m):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k-1:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output