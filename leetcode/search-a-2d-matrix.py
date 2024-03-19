class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cur=[]
        for i in matrix:
            cur.extend(i)
        
        l = 0
        r = len(cur)-1
        while l <= r:
            mid = (l+r)//2
            if cur[mid] > target:
                r = mid-1
            elif cur[mid] < target:
                l = mid+1
            else:
                return True
        return False
