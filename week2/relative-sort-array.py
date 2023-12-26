class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count={}
        arr1.sort()
        res=[]
        count2={}
        
        for i in arr2:
            count2[i] = 1+ count.get(i,0)
        
        for i in arr1:
            count[i] = 1+count.get(i,0)
        for i in arr2:
            for j in range(count.get(i)):
                res.append(i)
        for i in arr1:
            if i not in count2:
                res.append(i)
        print(count)
        return res
