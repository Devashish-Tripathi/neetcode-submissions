import functools
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {target: 1}
        def search(curr_val):
            if curr_val == target:
                return 1
            elif curr_val > target:
                return 0
            elif curr_val in dp:
                return dp[curr_val]
            ans = 0
            for i in nums:
                ans += search(curr_val + i)
            dp[curr_val] = ans
            return ans
        return search(0)