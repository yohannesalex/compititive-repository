# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA=0
        cura=headA
        while cura:
            cura=cura.next
            lenA+=1
        lenB=0
        curb=headB
        while curb:
            curb=curb.next
            lenB+=1
        
        if lenB > lenA:
            k=lenB-lenA
            curb=headB
            
            while k>0 and curb:
                curb=curb.next
                k-=1
            cura=headA
            while cura and curb:
                if cura == curb:
                    return cura
                cura=cura.next
                curb=curb.next
            return
        elif lenA > lenB:
            k=lenA-lenB
            cura=headA
            
            while k>0 and cura:
                cura=cura.next
                k-=1
            curb=headB
            while cura and curb:
                if cura == curb:
                    return cura
                cura=cura.next
                curb=curb.next
            return
        else:
            curb=headB
            cura=headA
            while cura and curb:
                if cura == curb:
                    return cura
                cura=cura.next
                curb=curb.next
            return
        
        
        



                

        