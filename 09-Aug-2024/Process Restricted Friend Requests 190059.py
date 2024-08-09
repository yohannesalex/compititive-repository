# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        class DSU:
            def __init__(self, N, enemies):
                self.par = list(range(N))
                self.enemies = enemies

            def find(self, x):
                if self.par[x] != x:
                    self.par[x] = self.find(self.par[x])
                return self.par[x]

            def union(self, x, y):
                xr, yr = self.find(x), self.find(y)
                if xr == yr:
                    return True
                 
                # store the state before the union
                temp1 = xr
                temp2 = yr
                temp3 = self.par[yr]
                # now perform the union
                self.par[yr] = xr
                
                for i,j in self.enemies:
                    if self.find(i) == self.find(j):
                        # undo the union and return false
                        xr = temp1
                        yr = temp2
                        self.par[yr] = temp3
                        return False
                return True

        dsu = DSU(n, restrictions)
        
        res = []
        for i, j in requests:
            res.append(dsu.union(i,j))
        
        return res