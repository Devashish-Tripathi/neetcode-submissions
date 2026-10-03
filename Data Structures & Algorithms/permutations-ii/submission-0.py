class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recursion(nums, ans, curr, n, idcs, k):
            if k == n:
                ans.add(tuple(curr.copy()))
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
        
        ans = set()
        n = len(nums)
        recursion(nums, ans, [], n, set(), 0)
        return [list(x) for x in ans]