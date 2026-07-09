class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1
        for idx in range(n-2, -1, -1):
            if idx + nums[idx] >= goal:
                goal = idx
        if goal == 0:
            return True
        return False