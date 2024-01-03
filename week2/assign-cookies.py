class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res=0
        pt1=0
        pt2=0
        while pt1< len(g) and pt2< len(s):
            if g[pt1] <= s[pt2]:
                pt1+=1
                pt2+=1
                res+=1
            elif g[pt1] > s[pt2]:
                pt2+=1
        return res
