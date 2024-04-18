# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        graph = defaultdict(list)
        for n, m in prerequisites:
            graph[m].append(n)
            
        indegree=[0]*numCourses
        for cor, pre in prerequisites:
            indegree[cor]+=1
        que=deque()
        ans = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)
                
        
        
        
        while que:
            n = que.popleft()
            ans.append(n)
            for negn in graph[n]:
                
                indegree[negn]-=1
                if indegree[negn] == 0:
                    
                
                    que.append(negn)
        if numCourses != len(ans):
            return []
        return ans
        
