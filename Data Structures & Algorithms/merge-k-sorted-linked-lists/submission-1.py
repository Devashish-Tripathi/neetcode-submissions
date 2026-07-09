# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # dct = {x:0 for x in range(-1000, 1001)}
        # for ls in lists:
        #     while ls:
        #         dct[ls.val] += 1
        #         ls = ls.next
        
        # head = ListNode()
        # curr = head
        # for k, v in dct.items():
        #     while v > 0:
        #         temp = ListNode(k)
        #         curr.next = temp
        #         curr = temp
        #         v -= 1
        # return head.next 

        head = ListNode()
        curr = head
        k = len(lists)
        while True:
            minNode = -1
            for i in range(k):
                if not lists[i]: continue 
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i
            
            if minNode == -1:
                break
            
            curr.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            curr = curr.next
        
        return head.next
        