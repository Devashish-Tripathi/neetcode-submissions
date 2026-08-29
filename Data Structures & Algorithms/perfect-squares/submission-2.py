class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1] * (n+1)
        dp[0] = 0
        for val in range(1, n+1):
            for s in range(val+1):
                sq = s*s
                if val-sq > -1:
                    dp[val] = min(dp[val], dp[val-sq]+1)
                else:
                    break
        return dp[n]        