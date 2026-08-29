class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i <= math.sqrt(n):
            squares.append(i*i)
            i += 1

        dp = [n+1] * (n+1)
        dp[0] = 0
        for val in range(1, n+1):
            for sq in squares:
                if val-sq > -1:
                    dp[val] = min(dp[val], dp[val-sq]+1)
                else:
                    break
        return dp[n]        