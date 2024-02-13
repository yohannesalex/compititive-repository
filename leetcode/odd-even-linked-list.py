# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy1 = ListNode()
        dummy2 = ListNode()
        eve = dummy2
        od = dummy1
        cur = head
        while cur and cur.next:
            od.next=cur
            eve.next=cur.next
            od = od.next
            eve = eve.next
            cur = cur.next.next
            eve.next = None
            od.next= None
            
        if cur:
            od.next = cur
            od = od.next
            

        od.next = dummy2.next
        return dummy1.next
        