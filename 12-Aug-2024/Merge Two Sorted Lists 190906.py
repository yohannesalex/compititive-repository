# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        dummy = ListNode()
        merged= dummy
        cur1=list1
        cur2=list2
        while cur1 and cur2:
            if cur1.val >= cur2.val:
                merged.next=cur2
                cur2=cur2.next
            else:
                merged.next = cur1
                cur1=cur1.next
            merged = merged.next
        if not cur1:
            
            merged.next = cur2
            
        elif not cur2:
            
            merged.next = cur1
        return dummy.next

        