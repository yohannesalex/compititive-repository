# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        to_list = []
        cur = head
        
        while cur:
            to_list.append(cur.val)
            cur=cur.next
        maxi = 0
        n = len(to_list)
        for i in range(len(to_list)):
            if 0 <= i <= (n / 2) - 1:
                maxi = max(to_list[i]+ to_list[n-1-i], maxi)
        return maxi
