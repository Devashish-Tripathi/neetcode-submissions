class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        left = 0
        currSum = 0
        for right in range(n):
            currSum += nums[right]
            while currSum >= target:
                ans = min(ans, right-left+1)
                currSum -= nums[left]
                left += 1
        return ans if left else 0