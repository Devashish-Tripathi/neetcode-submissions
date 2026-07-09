class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)
        for i in range(n):
            pr = prices[i]
            for j in range(i+1, n):
                maxprofit = max(maxprofit, prices[j]-pr)
        
        return maxprofit