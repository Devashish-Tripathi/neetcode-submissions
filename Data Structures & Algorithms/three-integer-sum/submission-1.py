class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    ans.add(tuple(sorted([nums[i], nums[j], -(nums[i] + nums[j])])))
        return [list(i) for i in ans]
