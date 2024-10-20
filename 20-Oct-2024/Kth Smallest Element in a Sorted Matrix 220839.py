# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # tot = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         tot.append(matrix[i][j])
        # heapify(tot)
        # for i in range(k):
        #     cur = heapq.heappop(tot)
        # return cur
        for i in range(len(matrix)):
            heapq.heapify(matrix[i])
        
        
        for j in range(k):
            res = matrix[0][0]
            heapq.heappop(matrix[0])
            if not len(matrix[0]):
                heapq.heappop(matrix)
            else:
                cur = matrix[0]
                heapq.heappop(matrix)
                heapq.heappush(matrix,cur)
        return res
