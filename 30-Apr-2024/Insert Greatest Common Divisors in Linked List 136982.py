# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next
        while cur:
            val1 = prev.val
            val2 = cur.val
            gcds = math.gcd(val1,val2)
            new = ListNode(gcds)
            prev.next = new
            new.next = cur
            prev = cur
            cur = cur.next
        return head