# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from queue import PriorityQueue

        def manhattanDistance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        def find(parent, child):
            if parent[child] == child:
                return child
            
            return find(parent, parent[child])
        
        def union(parent, child1, child2):
            root1 = find(parent, child1)
            root2 = find(parent, child2)

            if root1 != root2:
                parent[root1] = root2
        
        def formsCycle(parent, child1, child2):
            return find(parent, child1) == find(parent, child2)

        
        edges = PriorityQueue()
        for idx1 in range(len(points)):
            for idx2 in range(idx1 + 1, len(points)):
                distance  = manhattanDistance(points[idx1][0], points[idx1][1], points[idx2][0], points[idx2][1])
                edges.put((distance, idx1, idx2))
        
        minimumCost = 0
        count = len(points) - 1

        parent = [child for child in range(len(points))]
        
        while count > 0:
            
            cost, child1, child2 = edges.get()

            if formsCycle(parent, child1, child2):
                continue
            
            union(parent, child1, child2)
            
            minimumCost += cost
            count -= 1
        
        return minimumCost

                