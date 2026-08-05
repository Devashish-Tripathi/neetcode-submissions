class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = {}
        travels = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(heights), len(heights[0])
        rng_r, rng_c = range(m), range(n)
        heap = [(0, 0, 0)] # mad, x, y

        while heap:
            mad, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            if x==m-1 and y==n-1:
                return mad
            visited[(x, y)] = mad
            for dx, dy in travels:
                nx, ny = x+dx, y+dy
                if nx in rng_r and ny in rng_c:
                    nx_mad = max(mad, abs(heights[nx][ny]-heights[x][y]))
                    if (nx, ny) not in visited or visited[(nx, ny)] > mad:
                        heapq.heappush(heap, (nx_mad, nx, ny))
        print(visited)
        return visited[(m-1, n-1)]
