class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minV, maxV = min(nums), max(nums)
        if maxV <= 0:
            return 1
        
        dct = {x:0 for x in range(1, maxV+2)}
        for num in nums:
            if num > 0:
                dct[num] += 1
        
        for k, v in dct.items():
            if v == 0:
                return k
        