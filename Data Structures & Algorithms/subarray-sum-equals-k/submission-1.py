class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = currSum = 0
        prefixSum = {0:1}
        for num in nums:
            currSum += num
            diff = currSum-k
            ans += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        # print(prefixSum)
        return ans
        