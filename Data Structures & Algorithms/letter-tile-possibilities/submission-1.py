class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = [0] * 26
        for ch in tiles:
            counts[ord(ch)-65] += 1
        def dfs():
            total = 0
            for i in range(26):
                if counts[i]:
                    counts[i] -= 1
                    total += 1 + dfs()
                    counts[i] += 1
            return total
        return dfs()