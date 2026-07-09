class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if x == 0: return 0
        elif n == 0: return 1
        elif n == 1: return x
        x = 1/x if n < 0 else x
        
        ls = [x]*abs(n)
        while len(ls)>1:
            temp = []
            m = len(ls)
            i = 0
            while i+1<m:
                temp.append(ls[i]*ls[i+1])
                i = i+2
            if i==m-1:
                temp.append(ls[i])
            ls = temp

        return ls[0]

        # 2,2,2,2,2
        # 4,4,2
        # 16,2
        # 32
        # for i in range(0, n, 2):
        #     ls[i] *= ls[i+1]         



        # for i in range(abs(n)):
        #     ans *= x
        # return ans