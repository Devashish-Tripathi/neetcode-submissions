class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        b = sum([int(ch) for ch in bin(n)[2:]])
        return b==1