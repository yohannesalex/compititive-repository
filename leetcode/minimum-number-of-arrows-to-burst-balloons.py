class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        pt=points
        r=1
        count=0
        if len(points) ==1:
            return 1
        while r < len(points):
            while r<len(points) and points[r-1][1] >= points[r][0]:
                points[r]=[max(points[r][0],points[r-1][0]), min(points[r-1][1],points[r][1])]
                r+=1
            
            r+=1
            count+=1
        r-=1            
        
        if points[r-1][1] < pt[-1][0]:
            count+=1
        return count

        