class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) <3:
            return False
        stack=[]
        mini=nums[0]
       
        for i in range(1,len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            
            if stack and nums[i] > stack[-1][1]:
                return True
           
            stack.append([nums[i],mini])
            mini=min(nums[i],mini)
            
        return False
            

        

