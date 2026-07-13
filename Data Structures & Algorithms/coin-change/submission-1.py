class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for amt in range(1, amount+1):
            for coin in coins:
                if amt - coin >= 0:
                    # since we need minimum number of coins
                    dp[amt] = min(dp[amt], dp[amt-coin]+1)
            # if dp[amt] == amount+1:
                # return -1
        
        return dp[-1] if dp[-1] != amount+1 else -1

