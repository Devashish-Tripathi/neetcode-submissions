# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # go through the list and see how many k groups are there
        def get_kth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0, head)
        prevTemp = dummy
        while True:
            kth = get_kth(prevTemp, k)
            if not kth:
                break
            nextTemp = kth.next

            prev, curr = kth.next, prevTemp.next
            while curr != nextTemp:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = prevTemp.next
            prevTemp.next = kth
            prevTemp = temp
        return dummy.next
