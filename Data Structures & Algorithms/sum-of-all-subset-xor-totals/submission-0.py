class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]
        ans = 0
        for num in nums:
            subsets += [[num]+x for x in subsets]
        for subset in subsets:
            curr_t = 0
            for elem in subset:
                curr_t ^= elem
            ans += curr_t
        
        return ans