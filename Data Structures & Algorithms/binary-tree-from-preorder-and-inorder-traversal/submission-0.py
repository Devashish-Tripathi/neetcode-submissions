# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder is NLR
        # inorder is LNR
        self.pre_idx = 0
        idx = {val:i for i, val in enumerate(inorder)}
        def dfs(l, r):
            if l > r:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(val)
            mid = idx[val]
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)
            return node
        
        return dfs(0, len(inorder)-1)