class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        chars = set(s)
        for ch in chars:
            count = 0
            left = 0
            for i in range(n):
                if s[i] == ch:
                    count += 1
                while (i-left+1) - count > k:
                    if s[left] == ch:
                        count -= 1
                    left += 1
                
                ans = max(ans, i-left+1)
        return ans
