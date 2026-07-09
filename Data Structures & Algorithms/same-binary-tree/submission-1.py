# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def inorder(self, node, inorder):
        if node is None:
            inorder.append(None)
            return
        self.inorder(node.left, inorder)
        inorder.append(node.val)
        self.inorder(node.right, inorder)

    def preorder(self, node, preorder):
        if node is None:
            preorder.append(None)
            return
        preorder.append(node.val)
        self.preorder(node.left, preorder)
        self.preorder(node.right, preorder)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        in_1, in_2, pre_1, pre_2 = [], [], [], []
        self.inorder(p, in_1)
        self.inorder(q, in_2)
        self.preorder(p, pre_1)
        self.preorder(q, pre_2)
        if in_1 == in_2 and pre_1 == pre_2:
            return True
        return False