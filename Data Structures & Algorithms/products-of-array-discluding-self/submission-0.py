class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        zero_idx = -1
        prod = 1
        for i, num in enumerate(nums):
            if num == 0:
                if zero_idx == -1:
                    zero_idx = i
                else:
                    return [0]*n
            else:
                prod *= num

        if zero_idx != -1:
            output = [0]*n
            output[zero_idx] = prod
        else:
            for num in nums:
                output.append(prod//num)
        return output
