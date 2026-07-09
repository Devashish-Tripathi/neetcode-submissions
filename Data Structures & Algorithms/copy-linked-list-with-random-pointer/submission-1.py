"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        newList = Node(0)
        curr = newList
        temp = head
        ls_old, ls_new = [], []
        length = 0
        while temp:
            ls_old.append(temp)
            temp = temp.next
            length += 1
        
        temp = head
        k = 0
        while temp:
            k += 1
            curr.val = temp.val
            if k == length:
                ls_new.append(curr)
                break
            curr.next = Node(0)
            ls_new.append(curr)
            temp = temp.next
            curr = curr.next


        curr = newList
        for node in ls_old:
            idx = -1
            if node.random:
                idx = ls_old.index(node.random)
            if idx != -1:
                # print(length, k, idx)
                curr.random = ls_new[idx]
            curr = curr.next
        
        return newList