import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            num = random.choice(nums)
            if nums.count(num) > n//2:
                return num