"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        dct = {}
        def dfs(node):
            if node in dct:
                return dct[node]
            
            copy = Node(node.val)
            dct[node] = copy
            for nbr in node.neighbors:
                copy.neighbors.append(dfs(nbr))
            return copy
        
        return dfs(node)
        