# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ancestors = [set() for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        graph = defaultdict(list)
        for u , v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        que = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)
        
        while que:
            node = que.popleft()
            for neb in graph[node]:
                ancestors[neb].add(node)
                ancestors[neb].update(ancestors[node])
                indegree[neb] -= 1

                if indegree[neb] == 0:
                    que.append(neb)
        res = []
        for i , j in queries:
            if i in ancestors[j]:
                res.append(True)
            else:
                res.append(False)
        return res
