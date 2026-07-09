# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        def bfs(node, visited):
            queue = collections.deque([])
            queue.append(node)
            while queue:
                local = []
                curr_len = len(queue)
                for _ in range(curr_len):
                    node = queue.popleft()
                    if node:
                        local.append(node.val)                    
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                visited.append(local)

        visited = []
        bfs(root, visited)

        return visited