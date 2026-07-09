# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        nodes = []
        n = 0
        while temp:
            nodes.append(temp)
            temp = temp.next
            n += 1
        newNodes = [None] * n
        k = 0
        for i in range(n):
            if i % 2:
                newNodes[i] = nodes[n-k]
            else:
                newNodes[i] = nodes[k]
                k += 1
        for i in range(n-1):
            newNodes[i].next = newNodes[i+1]
        newNodes[-1].next = None
        head = newNodes[0]