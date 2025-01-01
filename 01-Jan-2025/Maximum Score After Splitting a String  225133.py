# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        start=s.count("1")
        res=float(-inf)
        
        for i in range(len(s)-1):
            if s[i] =="0":
                start+=1
                res=max(res,start)
            else:
                start-=1
                res=max(res,start)
        return res