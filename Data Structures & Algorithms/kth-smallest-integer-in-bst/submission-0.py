# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, node, order):
        if node is None:
            return
        self.inorder(node.left, order)
        order.append(node.val)
        self.inorder(node.right, order)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        self.inorder(root, order)
        return order[k-1]