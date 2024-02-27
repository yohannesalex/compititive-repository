class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        def sub(k):
            
            if k >= len(nums):
                res.append(path.copy())
                return 
            path.append(nums[k])
            sub(k+1)
            path.pop()
            sub(k+1)
        
        sub(0)
        return res