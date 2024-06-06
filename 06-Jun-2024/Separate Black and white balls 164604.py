# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        S = list(s)
        if len(s) == 1:
            return 0
        l = 0
        r = 1
        ans = 0
        while l < len(s) and r < len(s):
            if S[l] == "1" and S[r] == "0":
                ans+=r-l
                S[l] , S[r] = S[r] , S[l]
                l += 1
                r+=1
            elif S[l] == "1" and S[r] == "1":
                r+=1
            else:
                l+=1
                r+=1
        return ans
            
            
