class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if mid-1 > -1 and nums[mid] < nums[mid-1]:
                hi = mid-1
            elif mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                lo = mid+1
            else:
                return mid
