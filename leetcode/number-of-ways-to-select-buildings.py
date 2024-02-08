class Solution:
    def numberOfWays(self, s: str) -> int:
        zcount=0
        ocount=0
        pre=[0]*len(s)
        post=[0]*len(s)
        for i in range(len(s)):
            if s[i]=="0":
                zcount+=1
                pre[i]=[zcount,ocount]
            else:
                ocount+=1
                pre[i]=[zcount,ocount]
        zcount=0
        ocount=0
        for i in range(len(s)-1,-1,-1):
            
            if s[i]=="0":
                zcount+=1
                post[i]=[zcount,ocount]
            else:
                ocount+=1
                post[i]=[zcount,ocount] 
        
        res=0
        for i in range(1,len(s)-1):
            if s[i]=="0":
                res+=(pre[i][1]*(post[i+1][1]))
            else:
                res+=(pre[i][0]*(post[i+1][0]))
        return res
