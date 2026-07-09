class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        num_el = n*n
        freeze = set()
        for i in range(n):
            for j in range(n):
                temp1 = matrix[j][n-i-1]
                temp2 = matrix[n-i-1][n-j-1]
                temp3 = matrix[n-j-1][i]
                
                if (j, n-i-1) not in freeze:
                    matrix[j][n-i-1] = matrix[i][j]
                    freeze.add((j, n-i-1))

                if (n-i-1, n-j-1) not in freeze:
                    matrix[n-i-1][n-j-1] = temp1
                    freeze.add((n-i-1, n-j-1))

                if (n-j-1, i) not in freeze:
                    matrix[n-j-1][i] = temp2
                    freeze.add((n-j-1, i))
                
                if (i, j) not in freeze:
                    matrix[i][j] = temp3
                    freeze.add((i, j))

            if len(freeze) == num_el:
                break