class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        gm=[]
        playerMove=abs(target[0] )+ abs( target[1])
        for i in range(len(ghosts)):
            gm = abs(ghosts[i][0]-target[0])+ abs(ghosts[i][1]-target[1])
            if gm <= playerMove:
                return False
        return True

