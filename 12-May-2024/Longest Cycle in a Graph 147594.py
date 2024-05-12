# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        v=[0]*len(edges)
        ans=-1
        for i in range(len(edges)):
            t=1
            c=i
            while c>=0:
                if v[c]!=0:
                    if v[c][0]==i:
                        ans=max(ans,t-v[c][1])
                    break
                else:
                    v[c]=[i,t]
                    t+=1
                    c=edges[c]
        return ans
