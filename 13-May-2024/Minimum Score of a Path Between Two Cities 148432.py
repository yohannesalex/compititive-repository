# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        size = n
        parents = {i:i for i in range(1 , size+1)}
        rank = defaultdict(int)

        def find(x):
        
            if x == parents[x]:
                return x
            par = find(parents[x])
            parents[x] = par
            return par
        
        def union(x, y):
       
            x = find(x)
            y = find(y)

            

            if x != y:
                if rank[x] > rank[y]:
                    parents[y] = x
                elif rank[x] < rank[y]:
                    parents[x] = y
                else:
                    parents[x] = y
                    rank[y] += 1
               
        
        for node in roads:
            union(node[0] , node[1])
        
        connected = find(1)

        roads.sort(key=lambda x : x[2])

        for node in roads:
            if find(node[0]) == connected or find(node[1]) == connected:
                return node[2]

            

