import random
class Solution:

    def __init__(self, w: List[int]):
        curr = 0
        s = sum(w)
        self.weights = [v/s for v in w]
        self.vals = range(len(w))

    def pickIndex(self) -> int:
        return random.choices(self.vals, self.weights)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()