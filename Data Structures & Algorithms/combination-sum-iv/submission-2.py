import functools
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {target: 1}
        @functools.cache
        def search(curr_val):
            if curr_val == target:
                return 1
            elif curr_val > target:
                return 0
            ans = 0
            for i in nums:
                ans += search(curr_val + i)
            return ans
        return search(0)