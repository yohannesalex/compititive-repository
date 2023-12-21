class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res=0
        for i in range( len(strs[0])):
            a=""
            for j in range(len(strs)):
                a+=strs[j][i]
            
            if list(a)!=sorted(a):
                res+=1


        return res