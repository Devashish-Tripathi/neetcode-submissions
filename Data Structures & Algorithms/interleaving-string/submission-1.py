class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1+n2 != n3:
            return False
        dp = {}
        def recursion(i, j, k):
            if i == n1 and j == n2 and k == n3:
                return True
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            if i < n1 and s1[i] == s3[k]:
                if recursion(i+1, j, k+1):
                    dp[(i, j, k)] = True
                    return dp[(i, j, k)]
            if j < n2 and s2[j] == s3[k]:
                if recursion(i, j+1, k+1):
                    dp[(i, j, k)] = True
                    return dp[(i, j, k)]
            
            dp[(i, j, k)] = False
            return dp[(i, j, k)]
        
        return recursion(0, 0, 0)
            