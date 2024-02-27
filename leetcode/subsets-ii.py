
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        visit=[]

        def sub(k):
            
            if k >= len(nums):
                m=Counter(path)
                if m not in visit:

                    res.append(path.copy())
                    visit.append(m)
                    
                return
            
            path.append(nums[k])
            
            sub(k+1)
            path.pop()
            sub(k+1)
        
        sub(0)
        return res