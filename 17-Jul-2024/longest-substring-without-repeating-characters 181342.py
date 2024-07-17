# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_char=[]
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in my_char:
                my_char.remove(s[l])
                l+=1
            my_char.append(s[r])
            res=max(res,r-l+1)

            
            
        return res