class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        
        def mat_mul(A, B):
            return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]]]
            
        power = n
        M = [[1, 1], [1, 0]]
        ans = [[1, 0], [0, 1]]
        while power > 0:
            ans = mat_mul(ans, M)
            power -= 1
        
        return ans[0][0]
            
