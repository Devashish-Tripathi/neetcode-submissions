class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key= lambda x: (x[0], -x[1]))
        dp = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if envelopes[j][1] > envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)