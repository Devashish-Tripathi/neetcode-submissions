class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtract(i, subset):
            ans.append(subset.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                subset.append(nums[j])
                backtract(j+1, subset)
                subset.pop()
        backtract(0, [])
        return ans