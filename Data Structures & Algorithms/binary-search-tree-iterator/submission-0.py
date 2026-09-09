# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = []
        self._iterate(root)
        # print(self.vals)        
        self.maxLen = len(self.vals)
        self.currPos = -1

    def next(self) -> int:
        self.currPos += 1
        return self.vals[self.currPos]

    def hasNext(self) -> bool:
        if self.currPos == self.maxLen-1:
            return False
        return True

    def _iterate(self, node):
        if not node:
            return
        self._iterate(node.left)
        self.vals.append(node.val)
        self._iterate(node.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()