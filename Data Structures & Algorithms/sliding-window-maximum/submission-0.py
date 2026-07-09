class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxs = []
        num_maxs = len(nums)-k+1
        for i in range(num_maxs):
            maxs.append(max(nums[i:i+k]))
        return maxs