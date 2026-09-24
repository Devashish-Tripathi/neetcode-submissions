class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        ns = sx+sx
        n = len(sx)
        for i in range(n):
            if ns[i] != ns[n-i-1]:
                return False
        return True