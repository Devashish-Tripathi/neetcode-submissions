class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(openP, closeP, currStr):
            if len(currStr) == n*2:
                ans.append("".join(currStr))
            else:
                if closeP < openP:
                # can close
                    dfs(openP, closeP + 1, currStr+")")
                if openP < n:
                # can open another
                    dfs(openP+1, closeP, currStr+"(")
        
        dfs(0, 0, "")
        return ans