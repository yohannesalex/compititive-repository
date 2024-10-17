# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        arr = [[-1]*n for _ in range(m)]
        cur = head
        i = 0 
        j = 0

        while cur:
            for _ in range(n):
                arr[i][j] = cur.val
                j+=1
                cur = cur.next
                if not cur:
                    return arr
            j-=1
            i+=1
            m-=1
            for _ in range(m):
                arr[i][j] = cur.val
                i+=1
                cur = cur.next
                if not cur:
                    return arr
            i-=1
            j-=1
            n-=1
            for _ in range(n):
                arr[i][j] = cur.val
                j-=1
                cur = cur.next
                if not cur:
                    return arr
            j+=1
            i-=1
            m-=1
            for _ in range(m):
                arr[i][j] = cur.val
                i-=1
                cur = cur.next
                if not cur:
                    return arr
            j+=1
            i+=1
            n-=1
        return arr
            

            




        
        