class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s//2

        visited = set()
        dp = {}
        def dfs(idx, currSum):
            if currSum == target:
                return True
            if currSum > target or idx == n:
                return False
            if (idx, currSum) in dp:
                return dp[(idx, currSum)]
            dp[(idx, currSum)] = dfs(idx+1, currSum+nums[idx]) or dfs(idx+1, currSum)
            return dp[(idx, currSum)]
            
        return dfs(0, 0)