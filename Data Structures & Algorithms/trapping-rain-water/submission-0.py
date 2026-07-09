class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [height[0]]
        result = 0
        rightMax = [0]*n
        rightMax[n-1] = height[n-1] 
        for i in range(1, n):
            leftMax.append(max(leftMax[i-1], height[i]))
            rightMax[n-i-1] = max(rightMax[n-i], height[n-i-1])
        
        for i in range(n):
            result += min(leftMax[i], rightMax[i])-height[i]
        
        return result