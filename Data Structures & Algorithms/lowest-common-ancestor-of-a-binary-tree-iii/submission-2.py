"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def height(node):
            ht = 0
            while node:
                node = node.parent
                ht += 1
            return ht
        
        hp, hq = height(p), height(q)
        # keep q deeper
        if hq < hp:
            p, q = q, p
            hp, hq = hq, hp
        
        diff = hq - hp
        while diff:
            q = q.parent
            diff -= 1
        
        while p != q:
            p = p.parent
            q = q.parent

        return p