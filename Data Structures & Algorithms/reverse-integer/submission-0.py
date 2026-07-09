class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0: 
            flag = True
        x = int(str(abs(x))[::-1])
        if flag:
            x = -x
        if x < -2**31 or x >= 2**31:
            return 0
        return x
