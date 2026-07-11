# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        biggest = -101
        ans = 0
        
        def dfs(node, biggest):
            nonlocal ans
            if not node:
                return
            if node.val >= biggest:
                ans += 1
                biggest = node.val
            
            dfs(node.left, biggest)
            dfs(node.right, biggest)
        
        dfs(root, biggest)
        return ans
            
            