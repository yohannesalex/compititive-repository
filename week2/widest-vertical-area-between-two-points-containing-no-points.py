class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxi=0
      
        for i in range(len(points)-1):
            maxi=max(maxi,points[i+1][0]-points[i][0])
        return maxi