class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        counts = Counter(sorted_s1)
        n1, n2 = len(s1), len(s2)
        for i in range(n2-n1+1):
            if sorted(s2[i:i+n1]) == sorted_s1:
                return True
        return False