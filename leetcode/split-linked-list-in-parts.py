# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp=head

        c=0
        while(temp):
            c+=1
            temp=temp.next
        temp=head
        size=c//k
        rem=c%k
        res=[]
        while(temp):
            if(rem>0):
                a=0
                h1=temp
                while(temp and a<size):
                    temp=temp.next
                    a+=1
                res.append(h1)
                if temp==None:
                    break
                m=temp.next
                temp.next=None
                temp=m
                rem-=1
            else:
                a=0
                h1=temp
                while(temp and a<size-1):
                    temp=temp.next
                    a+=1
                res.append(h1)
                if temp==None:
                    break
                m=temp.next
                temp.next=None
                temp=m
        if(k>c):
            for i in range(k-c):
                res.append(None)

        return res

            


        