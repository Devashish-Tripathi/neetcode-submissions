class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        nextG = {num: idx for idx, num in enumerate(nums1)}
        
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nextG[val]
                ans[idx] = curr
            if curr in nextG:
                stack.append(curr)
        return ans