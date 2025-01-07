# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[]
       
        for i in range(len(boxes)):
            cur=0
            l=0
            while l < len(boxes):
              
                if boxes[l]=="1":
                    cur+=abs(l-i)
                l+=1
            res.append(cur)
            cur=0
        return res