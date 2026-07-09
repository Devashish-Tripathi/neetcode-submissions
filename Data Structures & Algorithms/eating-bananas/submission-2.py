import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eat(k, h, piles):
            tot_time = 0
            for p in piles:
                tot_time += math.ceil(p/k)
                if tot_time > h:
                    return False
            if tot_time > h:
                return False
            else:
                return True


        left = 1
        right = max(piles)
        possibles = []
        while left <= right:
            mid = left + (right-left)//2
            if eat(mid, h, piles):
                possibles.append(mid)
                right = mid-1
            else:
                left = mid+1

        return min(possibles)

            
                