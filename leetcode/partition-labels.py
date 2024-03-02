class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count={}
        for i,c in enumerate(s):
           count[c]=i
        l=0
        r=0
        res=[]
        for i,c in enumerate(s):
            r = max(r,count[c])
            if r == i:
                res.append(r-l+1)
                l=r+1
        return res