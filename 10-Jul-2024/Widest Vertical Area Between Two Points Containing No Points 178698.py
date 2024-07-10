# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        x_cor = [i for i,j in points]

        x_cor.sort()
        ans = 0

        for i in range(len(x_cor)-1):
            if ans < x_cor[i+1] - x_cor[i]:
                ans = x_cor[i+1] - x_cor[i]  
        return ans
        