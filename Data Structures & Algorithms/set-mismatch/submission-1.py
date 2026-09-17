class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # givenSum = sum(nums)
        # actualSum = sum(range(1, n+1))
        # dup_min_miss = givenSum-actualSum
        
        # given = actual-missing+duplicate
        # duplicate-missing = given-actual
        ctr = {i:0 for i in range(1, len(nums)+1)}
        for num in nums:
            ctr[num] += 1
        dup, missing = -1, -1
        for num, cnt in ctr.items():
            if cnt == 2:
                dup = num
            if cnt == 0:
                missing = num
            # if dup != missing != -1:
                # break
        return [dup, missing]