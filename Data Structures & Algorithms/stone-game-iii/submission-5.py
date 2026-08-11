class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')]*(n+1)
        dp[n] = 0
        for i in range(n-1, -1, -1):
            stone = 0
            for j in range(i, min(i+3, n)):
                stone += stoneValue[j]
                dp[i] = max(dp[i], stone-dp[j+1])
        
        if dp[0] == 0:
            return "Tie"
        return "Alice" if dp[0] > 0 else "Bob"