class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        dp = {}
        def dfs(idx, curr_sum):
            nonlocal ans
            if idx == n:
                return curr_sum == target
            elif (idx, curr_sum) in dp:
                return dp[(idx, curr_sum)]
            else:
                dp[(idx, curr_sum)] = dfs(idx+1, curr_sum+nums[idx])+dfs(idx+1, curr_sum-nums[idx])
                return dp[(idx, curr_sum)]

        return dfs(0, 0)