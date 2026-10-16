class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute force O(n**2)
        n = len(nums)
        dp = [1]*n
        # dp[i] = dp[i+1] + 1 if LIS continues
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
            