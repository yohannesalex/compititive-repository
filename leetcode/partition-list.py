# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2= ListNode()
        less=dummy1
        great = dummy2
        cur = head
        while cur:
            
            if cur.val < x:
                less.next = cur
                less = less.next
                cur = cur.next
                less.next = None
            
            else:
                great.next = cur
                great = great.next
                cur = cur.next
                great.next = None
            
            
        gr = dummy2.next
        less.next = gr
        return dummy1.next