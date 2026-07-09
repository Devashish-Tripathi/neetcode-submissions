class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]
        k = 2
        while k < n:
            T.append(T[k]+T[k-1]+T[k-2])
            k += 1
        return T[n]