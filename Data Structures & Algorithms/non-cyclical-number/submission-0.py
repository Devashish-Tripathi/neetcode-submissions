class Solution:
    def isHappy(self, n: int) -> bool:
        numsList = set()
        while n != 1:
            if n in numsList:
                return False
            numsList.add(n)
            n = sum([int(x)*int(x) for x in str(n)])

        return True
