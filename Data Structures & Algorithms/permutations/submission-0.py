class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursion(nums, ans, curr, n, idcs, k):
            if k == n:
                ans.append(curr.copy())
                return
            for i in range(n):
                if i in idcs:
                    continue
                curr.append(nums[i])
                idcs.add(i)
                recursion(nums, ans, curr, n, idcs, k+1)
                curr.pop()
                idcs.remove(i)
            return
        
        ans = []
        n = len(nums)
        recursion(nums, ans, [], n, set(), 0)
        return ans