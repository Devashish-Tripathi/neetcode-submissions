class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx-1]:
                nums[k] = nums[idx]
                k += 1
        return k