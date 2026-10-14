class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        nums.sort()
        ans = []
        for i in range(1, len(nums)):
            if i == 1 and nums[i] != nums[0]:
                ans.append(nums[0])
            if nums[i] != nums[i-1]:
                if (i+1 < len(nums) and nums[i] != nums[i+1]) or i+1 == len(nums):
                    ans.append(nums[i])
        return ans