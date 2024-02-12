# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pt1= head
        pt2=head
        while pt2 and pt2.next:
            pt1=pt1.next
            pt2=pt2.next.next
        return pt1