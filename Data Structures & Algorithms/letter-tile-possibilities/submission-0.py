class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        visited = set()
        ans = set()
        def dfs(curr):
            if curr:
                ans.add(''.join(curr.copy()))
            for j in range(n):
                if j in visited:
                    continue
                # can use j
                visited.add(j)
                curr.append(tiles[j])
                dfs(curr)
                # can skip j
                visited.remove(j)
                curr.pop()
            return
        dfs([])
        return len(ans)