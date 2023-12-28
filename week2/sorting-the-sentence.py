class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(s.split())
        s.sort(key = lambda x:int(x[-1]))
        for i in range(len(s)):
            s[i] = s[i][0:len(s[i])-1]
        return " ".join(s)