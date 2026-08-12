class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        ans = []
        col, posDiag, negDiag = set(), set(), set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)
                
                board[r][c] = '.'
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)


        backtrack(0)
        return ans