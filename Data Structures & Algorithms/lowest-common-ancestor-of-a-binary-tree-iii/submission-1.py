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
        # go through q
        moves = 0
        ans = []
        q1 = q
        while q1.parent:
            if q1.val == p.val:
                ans.append((moves, p))
            moves += 1
            q1 = q1.parent
        # go through p
        moves = 0
        p1 = p
        while p1.parent:
            if q.val == p1.val:
                ans.append((moves, q))
            moves += 1
            p1 = p1.parent
        # go through both
        while p.parent and q.parent:
            if p.val == q.val:
                ans.append((moves, p))
            p = p.parent
            q = q.parent
            moves += 1
        
        if ans:
            return sorted(ans)[0][1]
        else:
            # if one of them isn't anymore, return that since its root
            if not p.parent:
                return p
            else:
                return q