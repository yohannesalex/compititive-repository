# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
        gcds = []
        while cur and cur.next:
            gcds.append(gcd(cur.val, cur.next.val))
            cur = cur.next
        cur = head
        i = 0
        while cur and i <len(gcds):
            newNode = ListNode(gcds[i])
            newNode.next = cur.next
            cur.next = newNode
            cur = cur.next
            cur = cur.next
            i+=1
        return head

