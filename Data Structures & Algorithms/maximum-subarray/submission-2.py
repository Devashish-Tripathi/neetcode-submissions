class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for elem in nums:
            curSum += elem
            maxSub = max(maxSub, curSum)
            if curSum < 0:
                curSum = 0
        return maxSub