class Solution:
    def minimizedStringLength(self, s: str) -> int:
        count={}
        for i in s:
            count[i]=1+count.get(i,0)
        return len(count)