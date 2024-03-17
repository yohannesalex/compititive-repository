class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        candidates.sort()
        def comb(pos,path, total):
            pre=-2
            if total == target:
                res.append(path.copy())
                return
            if  pos >= len(candidates) or total > target:
                return 
            for i in range(pos,len(candidates)):
                if candidates[i] == pre:
                    continue
                path.append(candidates[i])
                
                comb(i+1, path, total+candidates[i] )
                path.pop()
                pre = candidates[i]
                
            
        comb(0,[],0)
        
        return res