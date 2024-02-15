class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        while maxDoubles>0 and target != 1:
            if maxDoubles == 0:
                break
            elif target%2 !=0:
                ans+=1
                target-=1
            else:
                target =target//2
                maxDoubles-=1
                ans+=1
        if target != 1:
            ans+=target-1
        return ans
