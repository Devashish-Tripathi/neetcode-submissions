class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        c_nums = Counter(nums)
        for i in range(n):
            c_nums[nums[i]] -= 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                curr = nums[i]+nums[j]
                c_nums[nums[j]] -= 1

                if curr > 0:
                    break
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                
                if c_nums[-curr]:
                    ans.append([nums[i], nums[j], -curr])
                # c_nums[nums[j]] += 1
            
            for j in range(i+1, n):
                c_nums[nums[j]] += 1
        return ans
