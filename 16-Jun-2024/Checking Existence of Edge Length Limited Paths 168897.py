# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        union_find = UnionFind(n)
        
        for index, query in enumerate(queries):
            query.append(index)
        
        edgeList.sort(key=lambda x: x[2])
        queries.sort(key=lambda x: x[2])
        
        pointer = 0
        result = [False] * len(queries)
        for node1, node2, limit, original_index in queries:
            while pointer < len(edgeList) and edgeList[pointer][2] < limit:
                temp_node1, temp_node2, _ = edgeList[pointer]
                union_find.union(temp_node1, temp_node2)
                pointer += 1
                
            if union_find.connected(node1, node2):
                result[original_index] = True
                
        return result
