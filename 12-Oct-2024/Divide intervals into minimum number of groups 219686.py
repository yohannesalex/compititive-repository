# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()

        for item in intervals:
            start,end = item
            if heap and heap[0]<start:
                heapq.heappop(heap)
            
            heapq.heappush(heap,end)
        return len(heap)