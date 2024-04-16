# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        toList=[]
        
        for i in lists:
            cur=[]
            head = i
            while head:
                cur.append(head.val)
                head = head.next
            toList.append(cur.copy())
        tot = []
        for i in toList:
           tot.extend(i)
        heapify(tot)
        dummy=ListNode(0)
        cur = dummy
        for i in range(len(tot)):
            new = heapq.heappop(tot)
            node = ListNode(new)
            cur.next=node
            cur=cur.next
        return dummy.next


        

        
