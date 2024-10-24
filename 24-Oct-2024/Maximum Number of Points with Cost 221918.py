# Problem: Maximum Number of Points with Cost - https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev = points[0]
        
        for r in range(1, m):
            left = [0] * n
            right = [0] * n
            
            left[0] = prev[0]
            for c in range(1, n):
                left[c] = max(left[c-1], prev[c] + c)
            
            right[-1] = prev[-1] - (n-1)
            for c in range(n-2, -1, -1):
                right[c] = max(right[c+1], prev[c] - c)
            
            for c in range(n):
                prev[c] = points[r][c] + max(left[c] - c, right[c] + c)
        
        return max(prev)