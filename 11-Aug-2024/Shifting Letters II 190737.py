# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        k=[0]*(len(s)+1)
        
        for i in shifts:
            if i[2] == 1:

                k[i[0]]+=1
                k[i[1]+1]-=1
            else:
                k[i[0]]-=1
                k[i[1]+1]+=1
        pre=[k[0]]
        for i in k[1:]:
            pre.append(pre[-1]+i)
          
        
        stri=""
        for j in range(len(s)):
            i=ord(s[j]) - ord("a")
            i+=pre[j]
            i = i % 26
            i = i + ord("a")
            stri +=chr(i)
        return stri