# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def back(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j == len(triangle)-1:
                return triangle[j][i]
            tot = 0
            
            tot += triangle[j][i]+min( back(i,j+1) , back(i+1,j+1))
            memo[(i,j)] = tot
            return tot
        return back(0,0)
