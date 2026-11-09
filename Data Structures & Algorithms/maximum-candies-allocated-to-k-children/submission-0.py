class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low, high = 0, max(candies)
        while low < high:
            middle = (low+high+1)//2
            # print(low, middle, high)
            portions = sum(x//middle for x in candies)
            # print(portions)
            if portions >= k:
                low = middle
            else:
                high = middle-1
        return low