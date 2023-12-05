class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=0
        res=''
        ans=[]
        while l < len(num)-1:
            
            while l < len(num)-1 and num[l] == num[l+1]:
                res+=num[l]
                l+=1
            res+=num[l-1]
            if len(res) >= 3:
                ans.append(res[0:3])
            res=""
            l+=1
        inti=[]
        if ans: 
            for i in ans:
                inti.append(int(i))
            k=inti.index(max(inti))
            return ans[k]
        else:
            return ""
            