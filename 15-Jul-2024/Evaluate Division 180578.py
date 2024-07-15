# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.values = []
    def connect(self, connection, val):
        self.connections.append(connection)
        self.values.append(val)

    def getVal(self, b):
        for i, c in enumerate(self.connections):
            if b.name == c.name:
                return self.values[i]
        return -1

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = {}
        for i in range(len(equations)):
            a, b = equations[i]
            if a not in nodes:
                nodes[a] = Node(a)
            if b not in nodes:
                nodes[b] = Node(b)
            nodes[a].connect(nodes[b], values[i])
            nodes[b].connect(nodes[a], 1/values[i])

        def dfs(a, b, seen=[]):
            if a.name == b.name :
                return 1
            val = a.getVal(b)
            if val != -1:
                return val

            for c in a.connections:
                if c not in seen:
                    ac = a.getVal(c)
                    cb = dfs(c, b, seen + [c])
                    if ac != -1 and cb != -1:
                        return ac * cb
                    
            return -1

        res = []
        for query in queries :
            a, b = query
            if a in nodes and b in nodes:
                if a != b :
                    res.append(dfs(nodes[a], nodes[b]))
                else:
                    res.append(1)
            else:
                res.append(-1)
        return res