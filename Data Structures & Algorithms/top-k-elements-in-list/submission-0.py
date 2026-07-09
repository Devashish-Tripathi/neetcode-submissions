class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {x:0 for x in set(nums)}
        
        for num in nums:
            hmap[num] += 1
        
        return [ke for ke, _ in sorted(hmap.items(), key= lambda d: -d[1])][:k]