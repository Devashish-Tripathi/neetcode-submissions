class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        to_run = min(m, n)
        ans = ""
        for i in range(to_run):
            ans += word1[i]+word2[i]
        ans += word2[i+1:] if m<n else word1[i+1:]
        return ans