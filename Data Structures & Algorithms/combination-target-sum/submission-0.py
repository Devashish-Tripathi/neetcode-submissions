class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def func(curr_sum, ans, curr_arr, i, n):
            if curr_sum == target:
                ans.append(curr_arr.copy())
                return
            elif i >= n or curr_sum > target:
                return
            curr_arr.append(nums[i])
            func(curr_sum+nums[i], ans, curr_arr, i, n)
            curr_arr.pop()
            func(curr_sum, ans, curr_arr, i+1, n)


        ans = []
        n = len(nums)
        func(0, ans, [], 0, n)
        
        return ans
