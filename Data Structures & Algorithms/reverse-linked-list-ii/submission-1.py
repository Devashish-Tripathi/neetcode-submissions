# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        idx = 1
        prevTemp = dummy
        temp = head
        while idx < left:
            prevTemp = temp
            temp = temp.next
            idx += 1
        
        prev = None
        while idx <= right:
            tempNext = temp.next
            temp.next = prev
            prev = temp
            temp = tempNext
            idx += 1
        
        # prevTemp.next is the original first, now last node
        # but won't its next be None?, oh wait got it, it's next is None, we connect it to the end
        prevTemp.next.next = temp
        prevTemp.next = prev

        return dummy.next