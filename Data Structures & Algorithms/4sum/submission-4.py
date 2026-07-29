class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for a in range(n):
            # if nums[a] > target:
                # break
            for b in range(a+1, n):
                # if nums[a] + nums[b] > target:
                    # break
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                for c in range(b+1, n):
                    # if nums[a] + nums[b] + nums[c] > target:
                        # break
                    if c > b+1 and nums[c] == nums[c-1]:
                        continue
                    if target-(nums[a] + nums[b] + nums[c]) in nums[c+1:]:
                        ans.add((nums[a], nums[b], nums[c], target-(nums[a] + nums[b] + nums[c])))
            
        
        return [list(x) for x in ans]