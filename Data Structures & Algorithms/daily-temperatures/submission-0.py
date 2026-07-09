class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        n = len(temperatures)
        for i in range(n):
            count = 0
            temp = temperatures[i]
            j = i+1
            while j < n:
                if temperatures[j] > temp:
                    count += 1
                    break
                count += 1
                j += 1
            if j==n: count = 0
            results.append(count)
        return results
                