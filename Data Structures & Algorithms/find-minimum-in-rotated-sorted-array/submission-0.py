class Solution:
    def findMin(self, nums: List[int]) -> int:
        while nums[0] > nums[-1]:
            nums = [nums[-1]]+nums[:-1]
        return nums[0]