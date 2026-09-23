class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0
        local = 0
        for idx, num in enumerate(nums):
            if num == 1:
                local += 1
            else:
                maxC = max(maxC, local)
                local = 0
        return max(maxC, local)
