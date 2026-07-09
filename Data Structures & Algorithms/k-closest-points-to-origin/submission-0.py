class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [x**2+y**2 for x, y in points]
        merged = list(zip(distances, points))
        merged.sort()
        points = [point for _, point in merged]
        return points[:k]