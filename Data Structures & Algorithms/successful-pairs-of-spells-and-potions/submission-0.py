class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def binary_search(spell):
            low, hi = 0, len(potions)-1
            while low <= hi:
                mid = low + (hi-low)//2
                if potions[mid] * spell >= success:
                    hi = mid-1
                else:
                    low = mid+1
            return low
        ans = []
        for spell in spells:
            idx = binary_search(spell)
            ans.append(len(potions)-idx)
        return ans