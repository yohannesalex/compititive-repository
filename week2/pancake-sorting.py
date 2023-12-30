class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]
        a=sorted(arr)
        n=len(arr)
        l=-1
        while a != arr :
            ind=arr.index(a[l])
            res.append(ind +1)
            res.append(n)
            
            p=0
            r=ind
            while p < r:
                arr[r] , arr[p] = arr[p] , arr[r]
                p+=1
                r-=1
            p=0
            k=n-1
            while p < k:
                arr[k] , arr[p] = arr[p] , arr[k]
                p+=1
                k-=1
            n-=1
            l-=1
            
        return res