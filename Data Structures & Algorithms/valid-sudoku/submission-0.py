class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            ct = set()
            for elem in row:
                if elem == '.':
                    continue
                elif elem not in ct:
                    ct.add(elem)
                else:
                    return False
        for j in range(9):
            column = set()
            for i in range(9):
                elem = board[i][j]
                if elem == '.':
                    continue
                elif elem not in column:
                    column.add(elem)
                else:
                    return False
        grid_origins = [0, 3, 6]
        grid_moves = [0, 1, 2]

        for i in grid_origins:
            for j in grid_origins:
                grid = set()
                for x in grid_moves:
                    for y in grid_moves:
                        elem = board[i+x][j+y]
                        if elem == '.':
                            continue
                        elif elem not in grid:
                            grid.add(elem)
                        else:
                            return False
        return True
                       