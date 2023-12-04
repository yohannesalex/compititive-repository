class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=list(s.split())
        _max=len(max(s,key=lambda x:len(x)))
        res=[""]*_max
        for i in range(_max):
            cur=""
            for r in range(len(s)):
                if len(s[r]) <= i:
                    cur+=" "
                else:
                    cur+=s[r][i]
            res[i]=cur.rstrip()
            cur=""
            
           

        return res
            


                



