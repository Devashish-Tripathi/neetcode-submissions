class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        for row in matrix:
            if target > row[-1]:
                continue
            lo, hi = 0, n-1
            print('here')
            while lo <= hi:
                mid = lo + ((hi-lo)//2)
                print('here')
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    hi = mid-1
                elif row[mid] < target:
                    lo = mid+1
        return False