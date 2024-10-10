# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top="qwertyuiop"
        middle="asdfghjkl"
        bottom = "zxcvbnm"
        res=[]
        for i in words:
            t=0
            m=0
            b=0
            for j in i:
                if j.lower() in top:
                    t+=1
                elif j.lower() in middle:
                    m+=1
                elif j.lower() in bottom:
                    b+=1
            if len(i) == t:
                res.append(i)
            elif len(i) == m:
                res.append(i)
            elif len(i) == b:
                res.append(i)
        return res

