class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            output.append(sum([1 for x in bin(i)[2:] if x=='1']))
        return output