class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        n = len(heights)
        i, j = 0, n-1
        while i < j:
            currVol = (j-i)*min(heights[i], heights[j])
            maxVol = max(currVol, maxVol)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return maxVol