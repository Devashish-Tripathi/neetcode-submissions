# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def preorder(self, node, ans):
        if node is None:
            ans.append("$#")
            return
        ans.append("$"+str(node.val))
        self.preorder(node.left, ans)
        self.preorder(node.right, ans)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_str, subroot_str = [], []
        self.preorder(root, root_str)
        self.preorder(subRoot, subroot_str)
        rst = ''.join(root_str)
        sst = ''.join(subroot_str)
        return sst in rst