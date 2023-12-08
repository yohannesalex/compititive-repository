class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        k=""
        n=len(spaces)
        u=0
        for i in range(n):
            a=spaces[i]
            k+=s[u:a]
            k+=" " 
            u=spaces[i]
        k+=s[a:]
        return k
