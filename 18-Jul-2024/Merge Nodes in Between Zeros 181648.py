# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        cur_sum = 0
        dummy =  ListNode()
        ans = dummy
        while cur:
            if cur.val == 0 :
                ans.next = ListNode(cur_sum)
                ans = ans.next
                cur_sum = 0
            else:
                cur_sum+=cur.val
            cur = cur.next
        return dummy.next
