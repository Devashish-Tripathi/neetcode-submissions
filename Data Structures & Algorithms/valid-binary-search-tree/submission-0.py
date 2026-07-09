# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, node, ls):
        if not node:
            return
        self.inorder(node.left, ls)
        ls.append(node.val)
        self.inorder(node.right, ls)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ls = []
        self.inorder(root, ls)
        for i in range(len(ls)-1):
            if ls[i] >= ls[i+1]:
                return False
        
        return True