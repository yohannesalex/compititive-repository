class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count={"W":0 , "B":0}
        for i in range(k):
            count[blocks[i]] = 1 + count.get(blocks[i],0)
       
        l=0
        r=k
        mini=float("inf")
        while r < len(blocks):
            mini=min(mini,count["W"])

            count[blocks[r]] = 1 + count.get(blocks[r],0)
            count[blocks[l]]-=1
            l+=1
            r+=1
        mini=min(mini,count["W"])
        
        return mini

