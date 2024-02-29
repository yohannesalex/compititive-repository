class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
		
        nums = tickets 
        time = 0
	
        least = nums[k]     
		
        for i in range(len(nums)):                  
            if k < i and nums[i] >= least :         
                time += (least - 1)
            elif nums[i] < least :                   
                time += nums[i]
            else:                                           
                time += least
				
        return time