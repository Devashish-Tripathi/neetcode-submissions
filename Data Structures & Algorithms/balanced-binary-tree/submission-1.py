# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def postorder(self, node, vals):
        if node is None:
            return 0
        
        lh_node = self.postorder(node.left, vals)
        rh_node = self.postorder(node.right, vals)

        print(node.val, lh_node, rh_node)
        if abs(lh_node-rh_node) > 1:
            vals.append(1)
        
        return 1+max(lh_node, rh_node)
        


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        vals = []
        self.postorder(root, vals)
        return len(vals) == 0