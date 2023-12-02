class Solution:
    def romanToInt(self, s: str) -> int:
        mapper={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
       
        res=mapper.get(s[0])
        cur=res
        
        for i in range(1,len(s)):
            
            if s[i-1]=="I" and s[i]=="V":
                res-=cur
                res+=4
            elif s[i-1]=="I" and s[i] =="X":
                res-=cur
                res+=9
            elif s[i-1]=="X" and s[i] == "L":
                res-=cur
                res+=40
            elif s[i-1]=="X" and s[i] == "C":
                res-=cur
                res+=90
            elif s[i-1]=="C" and s[i] == "D":
                res-=cur
                res+=400
            elif s[i-1]=="C" and s[i] == "M":
                res-=cur
                res+=900
            else:
                cur=mapper.get(s[i])
                res+=cur
        return res

