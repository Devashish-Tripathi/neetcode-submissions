class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        sys.setrecursionlimit(len(stoneValue) + 100)

        dp = {}
        def solve(idx):
            if idx >= len(stoneValue):
                return 0
            elif idx in dp:
                return dp[idx]
            max_score = float("-inf")
            stone = 0
            for i in range(idx, min(idx+3, len(stoneValue))):
                stone += stoneValue[i]
                score = stone - solve(i+1)
                max_score = max(max_score, score)
            
            dp[idx] = max_score
            return max_score
        
        ans = solve(0)
        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        else:
            return "Tie"