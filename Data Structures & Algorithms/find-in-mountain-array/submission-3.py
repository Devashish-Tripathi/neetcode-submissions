class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        size = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]
        
        # first find peak silly
        lo, hi = 0, size - 1
        while lo <= hi:
            mid = (hi+lo)//2
            left, middle, right = get(mid-1), get(mid), get(mid+1)
            if left < middle < right:
                lo = mid + 1
            elif left > middle > right:
                hi = mid - 1
            else:
                break
        
        peak = mid


        # two binary searches?
        # first do in first half
        lo, hi = 0, peak-1
        while lo <= hi:
            mid = (hi+lo)//2
            val = get(mid)
            if val == target:
                return mid
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        lo, hi = peak, size-1
        while lo <= hi:
            mid = (hi+lo)//2
            val = get(mid)
            if val == target:
                return mid
            elif val < target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1