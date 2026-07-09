class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [ch.lower() for ch in s if ch.isalnum()]
        return s_list == s_list[::-1]