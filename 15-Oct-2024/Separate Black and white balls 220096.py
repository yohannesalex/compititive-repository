# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == '0':
                ans+=i - count
                count+=1
        
        return ans

