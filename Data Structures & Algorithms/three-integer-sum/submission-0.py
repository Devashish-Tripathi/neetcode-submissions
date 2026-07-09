class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    ans.append(sorted([nums[i], nums[j], -(nums[i] + nums[j])]))
        ans = sorted(ans)
        dedup = [ans[i] for i in range(len(ans)) if i == 0 or ans[i] != ans[i-1]]
        return dedup