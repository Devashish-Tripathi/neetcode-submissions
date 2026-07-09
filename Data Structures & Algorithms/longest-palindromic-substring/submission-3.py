class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ansIdx = 0
        ansLen = 0
        for i in range(n):
            # odd length
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > ansLen:
                    ansLen = r-l+1
                    ansIdx = l
                l -= 1
                r += 1
            # even length
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > ansLen:
                    ansLen = r-l+1
                    ansIdx = l
                l -= 1
                r += 1

        
        return s[ansIdx:ansIdx+ansLen]