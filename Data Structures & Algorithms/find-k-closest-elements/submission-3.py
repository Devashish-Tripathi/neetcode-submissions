class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        lo, hi = 0, n-1
        closest, closest_idx = arr[0], 0
        while lo < hi:
            mid = lo + (hi-lo)//2            
            if arr[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        
        left, right = lo-1, lo
        sz = 0
        while sz < k and left >= 0 and right < n:
            if abs(arr[left]-x) <= abs(arr[right]-x):
                left -= 1
            else:
                right += 1
            sz += 1

        while sz < k and left >= 0:
            left -= 1
            sz += 1

        while sz < k and right < n:
            right += 1
            sz += 1 
        
        return arr[left+1:right]