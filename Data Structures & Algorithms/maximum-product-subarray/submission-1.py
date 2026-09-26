class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        currMax, currMin = 1, 1
        for num in nums:
            temp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(temp, num * currMin, num)
            ans = max(ans, currMax)
        return ans