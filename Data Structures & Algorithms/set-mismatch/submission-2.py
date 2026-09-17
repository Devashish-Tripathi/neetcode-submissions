class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup_min_miss = sum(nums) - sum(range(1, n+1))
        dup_plus_miss = (sum([num**2 for num in nums]) - sum([x**2 for x in range(1, n+1)]))//dup_min_miss
        dup = (dup_plus_miss+dup_min_miss)//2
        miss = dup-dup_min_miss
        return [dup, miss]
