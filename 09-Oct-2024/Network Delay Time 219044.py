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
            dis , curNode = heapq.heappop(heap)
            if curNode in processed:
                continue
            processed.add(curNode)
            for cost, child  in graph[curNode]:
                distance = min(distances[child], dis + cost)
                distances[child] = distance
                heapq.heappush(heap, [distance, child])
                    
            
        maxi = 0
        for key, val in distances.items():
            maxi = max(val, maxi)
        if maxi == float('inf'):
            return -1
        return maxi