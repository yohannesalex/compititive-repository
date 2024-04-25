# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans  = None
        
        rank = [1 for i in range(len(edges))]
        parents = {i:i for i in range(1,len(edges)+1)}
        def find(x):
            while x != parents[x]:
                x = parents[x] 
            return x
        res=[]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                
                parents[rootX] = rootY
                   
            else:
                return [x,y]
        
        for i in edges:
            ans = union(i[0],i[1])
            if ans:
                return ans
                
        