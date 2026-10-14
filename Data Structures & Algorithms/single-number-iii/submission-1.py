class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        # xor = a^b now
        # since both unique, so there is one set bit
        set_bit = 1
        while not xor & set_bit:
            set_bit <<= 1
        
        a = b = 0
        for num in nums:
            if set_bit & num:
                a ^= num
            else:
                b ^= num
        return [a, b]