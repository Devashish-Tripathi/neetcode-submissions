class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < len(numbers) and j >= 0:
            calc = numbers[i] + numbers[j] 
            if calc  ==  target:
                return [i+1, j+1]
            elif calc < target:
                i += 1
            else:
                j -= 1
