class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        r=0
        count={"T":0 , "F":0}
        maxi=0
        for r in range(len(answerKey)):
            count[answerKey[r]] = 1+count.get(answerKey[r],0)
            while min(count.values()) > k:
                count[answerKey[l]] -=1
                l+=1
            maxi=max(maxi,r-l+1)
            
        return maxi


