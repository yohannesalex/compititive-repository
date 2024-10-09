# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for i in times:
            graph[i[0]].append([i[2], i[1]])
        distances = {i: float('inf') for i in range(1,n+1)}
        distances[k] = 0
        processed = set()

        heap = [(0, k)]
        heapify(heap)
    
        while heap:
            # Write your code here
            dis , curNode = heapq.heappop(heap)
            if curNode in processed:
                continue
            processed.add(curNode)
            for cost, child  in graph[curNode]:
                
                distance =  dis + cost
                if distance < distances[child]:
                    distances[child] = distance
                    heapq.heappush(heap, [distance, child])
                    
        ans = max(distances.values())    
        if ans == float('inf'):
            return -1
        return ans