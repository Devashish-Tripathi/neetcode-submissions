class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def heist(amts):
            money = [0] * (n-1)
            money[0] = amts[0]
            money[1] = max(amts[0], amts[1])
            for i in range(2, n-1):
                money[i] = max(money[i-1], amts[i]+money[i-2])
            return max(money)

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        return max(heist(nums[1:]), heist(nums[:-1]))
        