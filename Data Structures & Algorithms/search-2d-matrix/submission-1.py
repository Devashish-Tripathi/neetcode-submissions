class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m-1
        while top <= bot:
            row = top+(-top+bot)//2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
        if not top <= bot:
            return False
        
        row_mat = matrix[row]
        lo, hi = 0, n-1
        while lo <= hi:
            mid = lo + ((hi-lo)//2)
            if row_mat[mid] == target:
                return True
            elif row_mat[mid] > target:
                hi = mid-1
            elif row_mat[mid] < target:
                lo = mid+1
        return False