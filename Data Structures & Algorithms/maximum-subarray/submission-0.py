class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -100000000000000000
        n = len(nums)
        for i in range(n):
            sub = nums[i:]
            k = n-i
            fullsum = sum(sub)
            maxSum = max(maxSum, fullsum)
            while k>=2:
                fullsum -= sub.pop()
                maxSum = max(maxSum, fullsum)
                k -= 1
        return maxSum