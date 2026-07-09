class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for elem in numSet:
            curr_len = 1
            if elem-1 not in numSet:
                while elem+curr_len in numSet:
                    curr_len += 1
            longest = max(longest, curr_len)
        return longest