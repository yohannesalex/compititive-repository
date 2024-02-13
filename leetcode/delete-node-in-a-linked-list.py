# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        cur=node
        temp=cur.next
        cur.val=temp.val
        cur.next= cur.next.next
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        