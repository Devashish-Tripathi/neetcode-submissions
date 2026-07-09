class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = {}
        for elem in nums:
            dct[elem] = dct.get(elem, 0) + 1
        for k, v in dct.items():
            if v==1: return k