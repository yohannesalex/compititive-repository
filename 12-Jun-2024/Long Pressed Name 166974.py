# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        if name == typed:
            return True
        
        i = 0
        j = 0
        while(i<len(name) and j < len(typed)):
            if name[i]!=typed[j]:
                return False
            pt1 = 0
            while(j+1 < len(typed) and typed[j]==typed[j+1]):
                j+=1
                pt1+=1
            pt2 = 0   
            while(i+1 < len(name) and name[i]==name[i+1]):
                i+=1
                pt2+=1
      
            if pt2 > pt1:
                return False
            
            i+=1
            j+=1
        
        
   
        if i != len(name) or j != len(typed):
            return False
        return True