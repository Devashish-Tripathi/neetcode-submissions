class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(idx):
            subarray = 1
            currSum  = 0
            for num in nums:
                currSum += num
                if currSum > idx:
                    subarray += 1
                    if subarray > k:
                        return False
                    currSum = num
            return True
        
        l, r = max(nums), sum(nums)
        ans = r
        while l <= r:
            mid = l + (r-l)//2
            if canSplit(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans