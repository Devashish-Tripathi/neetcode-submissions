class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set() # need it to be a set in case of duplicates in nums
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                break
            for j in range(i+1, n):
                curr = nums[i]+nums[j]
                if nums[j] > 0 and curr > 0:
                    break
                if -curr in nums[j+1:]:
                    ans.add((nums[i], nums[j], -curr))
        
        return [list(x) for x in ans]
