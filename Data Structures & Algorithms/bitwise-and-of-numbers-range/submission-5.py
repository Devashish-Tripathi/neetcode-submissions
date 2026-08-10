class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        n_bit_l, n_bit_r = (bin(left)[2:]), (bin(right)[2:])
        if len(n_bit_l) != len(n_bit_r):
            return 0
        ans = ''
        mismatch = False
        for i in range(len(n_bit_l)):
            if not mismatch and n_bit_l[i] == n_bit_r[i]:
                ans += n_bit_l[i]
            else:
                mismatch = True
                ans += '0'
        return int(ans, 2)
