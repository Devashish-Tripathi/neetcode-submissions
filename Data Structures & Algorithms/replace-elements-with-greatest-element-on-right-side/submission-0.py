class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxEl = -1
        ans = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            ans[i] = maxEl
            maxEl = max(maxEl, arr[i])
        return ans