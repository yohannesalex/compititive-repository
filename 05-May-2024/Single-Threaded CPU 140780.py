# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        minheap = []
        for cur in range(len(tasks)):
            heappush(heap, (tasks[cur][0], tasks[cur][1], cur))
        result = []
        span = 1

        while heap or minheap:
            if heap and not minheap and span < heap[0][0]: span = heap[0][0]
            while heap and heap[0][0] <= span:
                curr, time, idx = heappop(heap)
                heappush(minheap, (time, idx))
           
            
            time, idx = heappop(minheap)
            result.append(idx)
            span += time
        return result