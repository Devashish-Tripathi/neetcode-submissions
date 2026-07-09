class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            curr_s = s[i:]
            # print(i, curr_s)
            while curr_s:
                # print(curr_s)
                if curr_s ==  curr_s[::-1] and len(curr_s) >= len(ans):
                    ans = curr_s
                curr_s = curr_s[:-1]
        
        return ans