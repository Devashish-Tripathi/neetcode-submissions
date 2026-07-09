# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False 

        m = 0
        flag = False
        while m != 1001:
            m += 1
            head = head.next
            if not head:
                flag = True
                break
        
        return not flag