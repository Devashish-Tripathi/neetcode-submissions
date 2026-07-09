# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size = 0
        while temp is not None:
            temp = temp.next
            size += 1
        if size == 1:
            return
        elif size == 2:
            if n==1:
                head.next = None
                return head
            else:
                return head.next
            
        to_rem = size-n+1
        idx = 1
        node = head
        while idx < to_rem-1:
            node = node.next
            idx += 1
        if to_rem == 1:
            return head.next
        if node.next:
            node.next = node.next.next
        
        return head