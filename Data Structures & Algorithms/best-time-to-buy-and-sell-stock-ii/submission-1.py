class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(day, bought):
            if day == n:
                return 0
            elif (day, bought) in dp:
                return dp[(day, bought)]
            # do nothing
            ans = solve(day+1, bought)
            if bought:
                ans = max(ans, prices[day] + solve(day+1, False))
            else:
                ans = max(ans, -prices[day] + solve(day+1, True))
            dp[(day, bought)] = ans
            return ans

        n = len(prices)
        dp = {}
        return solve(0, False)