class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_pos, two_pos = 0, n-1
        i = 0
        while i <= two_pos:
            if nums[i] == 0:
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two_pos] = nums[two_pos], nums[i]
                two_pos -= 1
            else:
                i += 1