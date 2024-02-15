class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        tot=answers[0]+1
        checker={}
        checker[answers[0]]=answers[0]
        for i in range(1,len(answers)):
           
            
            if answers[i] == 0:
                tot+=1
            elif answers[i] not in checker:
                tot+=answers[i]+1
                checker[answers[i]] = answers[i]
            else:
                checker[answers[i]] -=1
                if checker[answers[i]] == 0:
                    del checker[answers[i]]
                
            
        return tot