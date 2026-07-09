# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # def gcd(a, b):
        #     # a is larger
        #     return a if b==0 else gcd(b, a%b)
        curr = head
        while curr.next:
            x, y = curr.val, curr.next.val
            a, b = max(x, y), min(x, y)
            temp = ListNode(val = math.gcd(a, b), next = curr.next)
            now_on = curr.next
            curr.next = temp
            curr = now_on
        return head