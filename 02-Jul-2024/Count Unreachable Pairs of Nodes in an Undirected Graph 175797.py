# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        nodes = set()
        for i in range(n):
            nodes.add(i)
        for i , j in edges:
            graph[i].append(j)
            graph[j].append(i)
            nodes.add(i)
            nodes.add(j)
        visited = set()
        def dfs(node):
            
            stack = [node]
            
            component_size = 0
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    component_size +=1
                    for nighbour in reversed(graph[current]):
                        if nighbour not in visited:
                            
                            stack.append(nighbour)
           
            return component_size
        collection = []
        prev = 0
        ans = 0
        for i in nodes:
            if i not in visited:
                
                collection.append(dfs(i))
        total_pairs = n*(n-1)//2
        reach_pairs = 0
        for i in collection:
            reach_pairs+=i *(i-1)//2
        return total_pairs - reach_pairs