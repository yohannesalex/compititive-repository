class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP=Counter(p)
        count={}
        res=[]
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            if r-l+1>len(p):
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1
            if r-l+1==len(p) and count==countP:
                res.append(l)
        return res


