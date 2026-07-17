class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        rng = range(n)
        for i in rng:
            if nums[i] < 0:
                nums[i] = 0
        
        for i in rng:
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val-1] > 0:
                    nums[val - 1] *= -1
                elif nums[val-1] == 0:
                    nums[val - 1] = -(n+1)
        
        for i in range(1, n+1):
            if nums[i-1] >= 0:
                return i
            
        return n+1
        