class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j, n = 0, 1, len(nums)

        while i < n and j < n:
            if nums[i] == nums[j]:
                return True
            j += 1
            if j - i > k:
                i += 1
                j = i+1
        
        return False
            
