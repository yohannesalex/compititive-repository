# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        prev = [float('inf') for i in range(n)]
        prev[src] = 0
        for i in range(k+1):
            cur = prev.copy()
            cur[src] = 0
            for u , v, w in flights:
                
               cur[v] = min(cur[v], prev[u] + w)
            prev = cur
        
        return cur[dst] if cur[dst] != float('inf') else -1

