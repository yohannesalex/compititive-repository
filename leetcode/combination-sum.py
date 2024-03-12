class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path=[]
        res=[]
        def comb(i,num, total):
            if total == target:
                res.append(path.copy())
                return 
            if i >= len(candidates) or total > target:
                return 
            path.append(candidates[i])
            comb(i, path, total+candidates[i])
            path.pop()
            comb(i+1, path, total )
        comb(0,[],0)
        return res
