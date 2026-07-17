class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        res = 0
        while lo <= hi:
            mid = lo + (hi-lo)//2
            sq = mid*mid
            if sq == x:
                return mid
            elif sq < x:
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res