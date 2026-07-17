class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        res = hi
        
        def canShip(cap):
            ship = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ship += 1
                    currCap = cap
                    if ship > days:
                        return False
                currCap -= w
            return True


        while lo <= hi:
            mid = (hi+lo)//2
            if canShip(mid):
                res = min(res, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        
        return res