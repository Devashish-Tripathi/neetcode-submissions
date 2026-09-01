class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def dfs(idx, numLeft):
            if idx == n and numLeft == 0:
                return 0
            elif idx == n or numLeft == 0:
                return float("inf")
            elif dp[idx][numLeft] != -1:
                return dp[idx][numLeft]
            else:
                ans = float("inf")
                currSum = 0
                for j in range(idx, n-numLeft+1):
                    currSum += nums[j]
                    ans = min(ans, max(currSum, dfs(j+1, numLeft-1)))

                dp[idx][numLeft] = ans
                return ans

        n = len(nums)
        dp = [[-1]*(k+1) for _ in range(n)]

        return dfs(0, k)