class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        self.length = len(self.nums)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        self.length += 1
        return self.nums[-self.k]