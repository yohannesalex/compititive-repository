class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        S=list(s)
         
        for l in range(0,len(s),2*k):
            r=min(l+k-1,len(S)-1)
            
            while r>l:
                S[l] , S[r] = S[r] , S[l]
                l+=1
                r-=1
            
            
        return "".join(S)