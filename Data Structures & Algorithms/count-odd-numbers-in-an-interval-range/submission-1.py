class Solution:
    def countOdds(self, low: int, high: int) -> int:
        size = high-low+1
        if low % 2 and size % 2:
            return size // 2 + 1
        return size // 2


