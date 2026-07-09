class Solution:
    def reverseBits(self, n: int) -> int:
        # return int(bin(n)[2:][::-1]+"0"*(32-len(bin(n)[2:])), 2)
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += bit << (31-i)
        return res