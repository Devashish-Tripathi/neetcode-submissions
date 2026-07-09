class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_pos = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: zero_pos.append((i, j))
        
        for x, y in zero_pos:
            matrix[x] = [0]*n
            for i in range(m):
                matrix[i][y] = 0
        
        