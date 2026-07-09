# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        values = []        
        def recurse(node, depth):
            if not node:
                return
            
            if depth == len(values):
                values.append(node.val)
            
            recurse(node.right, depth+1)
            recurse(node.left, depth+1)
        
        recurse(root, 0)
        return values