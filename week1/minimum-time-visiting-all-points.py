class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res=0
        for k in range(0,len(points)-1):
            res+=max(abs(points[k][0]-points[k+1][0]),abs(points[k][1]-points[k+1][1]))
        return res