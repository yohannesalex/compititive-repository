class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l=0 
        r= 0 
        res=0
        for i in range(len(s)):
            
            if s[i] == "(":
                l +=1
            else:
                
                if l > r:
                    r+=1
                else:
                    res +=1
                    
                
        
        res+=l-r
        return res