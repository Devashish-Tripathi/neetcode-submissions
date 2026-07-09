class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        n = len(s)
        currStr = {}
        idx = 0
        while idx < n:
            ch = s[idx]
            if ch in currStr:
                maxLen = max(maxLen, len(currStr))
                idx = currStr[ch] + 1
                currStr = {}
            else:
                currStr[ch] = idx
                idx += 1

        # for idx, ch in enumerate(s):
        #     if ch in currStr:
        #         maxLen = max(maxLen, len(currStr))
        #         currStr = set()
        #     currStr.add(ch)
        maxLen = max(maxLen, len(currStr))
        return maxLen
