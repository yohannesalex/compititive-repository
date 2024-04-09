# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for i, j in redEdges:
            red[i].append(j)
        for i, j in blueEdges:
            blue[i].append(j)

        ans = [-1 for i in range(n)]
        
        que = deque()
        visited = set()
        que.append([0,0,None])
        visited.add((0,None))
        while que:
            node , length , color = que.popleft()
            if ans[node] == -1:
                ans[node] = length
            if color!= "red":
                for negn in red[node]:
                    if (negn, "red") not in visited:
                        visited.add((negn, "red"))
                        que.append([negn,length+1,"red"])
            if color!= "blue":
                for negn in blue[node]:
                    if (negn, "blue") not in visited:
                        visited.add((negn, "blue"))
                        que.append([negn,length+1,"blue"])
        return ans
            


        