class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=0
        n=len(cardPoints)
        r=n-k
        cur=sum(cardPoints[0:r])
        mini=cur
        while r < n:
            cur-=cardPoints[l]
            cur+=cardPoints[r]
            mini=min(mini,cur)
            l+=1
            r+=1
        return sum(cardPoints)-mini

