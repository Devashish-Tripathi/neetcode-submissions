class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        answer = prices[:]
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                answer[stack.pop()] -= prices[i]
            stack.append(i)
        return answer