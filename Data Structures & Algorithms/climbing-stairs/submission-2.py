class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        
        def mat_mul(A, B):
            return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]
            
        power = n
        M = [[1, 1], [1, 0]]
        ans = [[1, 0], [0, 1]]
        while power:
            if power % 2 == 1:
                ans = mat_mul(ans, M)
            M = mat_mul(M, M)
            power //= 2
        
        return ans[0][0]
            
