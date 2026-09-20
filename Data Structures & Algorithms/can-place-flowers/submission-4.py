class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nums = len(flowerbed)
        if n == 0:
            return True
        if nums == 1:
            return not flowerbed[0]

        for i in range(nums):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == nums-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0