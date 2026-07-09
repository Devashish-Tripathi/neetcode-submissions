class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        money = [0] * n
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(2, n):
            money[i] = max(nums[i] + money[i-2], money[i-1])
        return money[-1]