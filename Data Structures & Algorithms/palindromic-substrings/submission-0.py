class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        for i in range(n):
            j = i+1
            k = i-1
            # odd length palindromes
            while k > -1 and j < n and s[j] == s[k]:
                dp[i] += 1
                j += 1
                k -= 1
            
            j = i+1
            k = i
            while k > -1 and j < n and s[j] == s[k]:
                dp[i] += 1
                j += 1
                k -= 1

        return sum(dp)