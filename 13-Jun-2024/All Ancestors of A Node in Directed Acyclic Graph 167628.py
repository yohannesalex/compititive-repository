# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
   
        def dfs(node):
            for next_node in graph[node]:
                if next_node not in cur_sq:
                    cur_sq.add(next_node)
                    dfs(next_node)
     
        graph = defaultdict(list)
        for x, y in edges:
            graph[y].append(x)

       
        ans = []
        for node_i in range(n):
            cur_sq = set()
            dfs(node_i)
            ans.append(sorted(list(cur_sq)))
            
        return ans
            