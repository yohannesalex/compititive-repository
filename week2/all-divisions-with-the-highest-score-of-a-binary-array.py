class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        tot=nums.count(1)
        count={0:tot}
        for i in range(1,len(nums)+1):
            if nums[i-1] == 0:
                k=tot+1
                count[i]=k
                tot+=1
            else:
                k=tot-1
                count[i] = k
                tot-=1
        
        
        
        sorted_nums = sorted(count.items(), key=lambda item: item[1])
        res=[]
        
        res.append(sorted_nums[len(sorted_nums)-1][0])
        
        for i in range(len(sorted_nums)-1,0,-1):
            
            if sorted_nums[i][1]== sorted_nums[i-1][1]:
                res.append(sorted_nums[i-1][0])
            else:
                break
        return res


