# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, ans):
            if node:
                ans.append(node.val)
                traverse(node.left, ans)
                traverse(node.right, ans)
        ans = []
        traverse(root, ans)
        return ans