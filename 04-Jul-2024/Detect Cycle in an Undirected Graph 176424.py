# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

def dfs(v, parent):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    visited = [False] * V
    for v in range(V):
        if not visited[v]:
            if dfs(v, -1):
                return True
    return False