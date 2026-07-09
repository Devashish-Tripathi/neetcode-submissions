class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digi = digits[-1] + 1
        carry = digi//10
        digits[-1] = digi%10
        n = len(digits)
        for i in range(1, n):
            digi = digits[n-i-1] + carry
            carry = digi//10
            digits[n-i-1] = digi%10

        if carry != 0:
            ls = [carry]
            ls.extend(digits)
            return ls
            
        
        return digits
