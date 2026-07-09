class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        step = 1
        ls = []
        count = 0
        x, y = 0, 0
        while count < m*n:
            if step==1:
                # row l to r
                section = matrix[x][y:n-y]
                ls.extend(section)
                count += len(section)
                step = 2
            
            elif step==2:
                # col t to d
                section = [row[n-y-1] for row in matrix[x+1:m-x]]
                ls.extend(section)
                count += len(section)
                step = 3

            elif step==3:
                # row r to l
                section = matrix[m-x-1][y:n-y-1][::-1]
                ls.extend(section)
                count += len(section)
                step = 4

            elif step==4:
                # col d to t
                section = [row[y] for row in matrix[x+1:m-x-1]][::-1]
                ls.extend(section)
                count += len(section)
                step = 1
                x += 1
                y += 1
            # print(step, section)
        return ls
