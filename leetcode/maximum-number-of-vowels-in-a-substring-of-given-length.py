class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow="aeiou"
        l=0
        r=k
        maxi=0
        count=0
        for i in range(k):
            if s[i] in vow:
                count+=1
        maxi=max(maxi,count)
        while r < len(s):
            if s[r]in vow:
                count+=1
            if s[l] in vow:
                count-=1
            maxi=max(maxi,count)
            
            r+=1
            l+=1
        return maxi
            

