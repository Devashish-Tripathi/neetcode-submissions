class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def dfs(num):
            if num in dp:
                return dp[num]
            ans = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num-i)
                ans = max(ans, val)
            dp[num] = ans
            return ans
        return dfs(n)
