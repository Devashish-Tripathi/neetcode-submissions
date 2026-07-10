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
        ans = []
        while sz < k and left >= 0 and right < n:
            if abs(arr[left]-x) <= abs(arr[right]-x):
                val = arr[left]
                left -= 1
            else:
                val = arr[right]
                right += 1

            ans.append(val)
            sz += 1

        while sz < k and left >= 0:
            ans.append(arr[left])
            left -= 1
            sz += 1

        while sz < k and right < n:
            ans.append(arr[right])
            right += 1
            sz += 1 
        
        return sorted(ans)