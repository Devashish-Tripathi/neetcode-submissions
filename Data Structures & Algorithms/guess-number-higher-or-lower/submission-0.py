# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # arr = list(range(1, n+1))
        lo = 1
        hi = n
        while lo <= hi:
            mid = lo + (hi-lo)//2
            check = guess(mid)
            if check == 0:
                return mid
            elif check == -1:
                hi = mid-1
            else:
                lo = mid+1
        
             