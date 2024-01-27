class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            permS1=Counter(s1)
            l=0
            r=len(s1)
            S2=""
            for i in range(len(s1)):
                S2+=s2[i]
            while r <= len(s2):
                permS2=Counter(S2)
                if permS1 == permS2:
                    return True
            
                l+=1
                r+=1
                S2=s2[l:r]            
                
            return False
