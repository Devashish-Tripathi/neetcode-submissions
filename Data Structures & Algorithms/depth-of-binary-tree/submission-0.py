# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def traversal(self, node, depth):
        if node is None:
            return depth
        depth += 1
        depth1 = self.traversal(node.left, depth)
        depth2 = self.traversal(node.right, depth)
        return max(depth1, depth2)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        return self.traversal(root, depth)
        