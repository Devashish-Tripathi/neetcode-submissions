class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True
        
        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(curr.copy())
                return
            if isPali(s, j, i):
                curr.append(s[j:i+1])
                dfs(i+1, i+1)
                curr.pop()
            dfs(j, i+1)

        res, curr = [], []        
        dfs(0, 0)
        return res