class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        l=0
       
        maxi=0
        processorTime.sort()
        tasks.sort(reverse = True)
        for i in range(len(tasks)):
          
            if (i)%4 ==0:
                maxi=max(maxi,processorTime[l]+tasks[i])
                
                l+=1
        return maxi
        
