class Solution:
    def reverseWords(self, s: str) -> str:
        new=list(s.split())
        new.reverse()
        return " ".join(new)
        
