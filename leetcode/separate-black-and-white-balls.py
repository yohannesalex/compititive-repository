class Solution:
    def minimumSteps(self, s: str) -> int:
        l=0
        r=1
        res=0
        S=list(s)
        while l < len(S) and r < len(S):
            if S[l]=="1" and S[r]=="0":
                S[l] , S[r] = S[r] , S[l]
                res+=(r-l)
                l+=1
                r+=1
            elif S[l] == "1" and S[r] =="1":
                r+=1
            elif S[l] == "0" and S[r] =="0":
                l+=1
                r+=1
            else:
                l+=1
                r+=1
        return res

