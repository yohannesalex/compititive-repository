class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        st=[]
        pre=0
        count={}
        res=0
        for i in nums:
            pre+=i
            st.append((pre)%k)
   
        for i in st:
            count[i]=1+count.get(i,0)
     
        for i in count:
            v=count.get(i)
            if i == 0:
                
                res+=v*(v-1)//2+v
            else:
                res+=v*(v-1)//2
        return res

