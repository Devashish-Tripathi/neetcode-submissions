from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = floor(n/3)
        numCounts = Counter()
        ans = set()
        for num in nums:
            numCounts[num] += 1
        for num in nums:
            if numCounts[num] > limit:
                ans.add(num)
        
        return list(ans)