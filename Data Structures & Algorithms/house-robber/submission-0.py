class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        money = [0] * n
        money[0] = nums[0]
        for i in range(1, n):
            maxVal = 0
            for j in range(i-1):
                maxVal = max(money[j], maxVal)
            money[i] = nums[i] + maxVal
        return max(money)