class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        count= defaultdict(lambda : True)
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                count[fronts[i]] = False

        mini=+inf
      
        for i in fronts+backs:
            if count[i] != False:
                mini=min(mini,i)
            
        if mini==+inf:
            return 0
        return mini


        