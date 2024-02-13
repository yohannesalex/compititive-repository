# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev= prev
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur=head
        cur.prev=None
        temp=cur
        while cur and cur.next:
            
            cur=cur.next
            cur.prev=temp
            temp=temp.next
        print(cur.val)
        back=cur
        forth=head
        while back and forth:
            if back.val != forth.val:
                return False
            back=back.prev
            forth=forth.next
        return True


        