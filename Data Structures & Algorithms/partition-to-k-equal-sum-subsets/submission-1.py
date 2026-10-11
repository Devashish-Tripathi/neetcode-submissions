class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums)//k
        nums.sort(reverse=True)
        used = [False] * len(nums)
        def dfs(i, k, currSum):
            if k == 0:
                return True
            if currSum == target:
                return dfs(0, k-1, 0)
            for j in range(i, len(nums)):
                if used[j] or currSum + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j+1, k, currSum+nums[j]):
                    return True
                used[j] = False
                if currSum == 0:
                    return False
            return False
        return dfs(0, k, 0)