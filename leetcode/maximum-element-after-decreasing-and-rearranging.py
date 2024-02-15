class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        count={}
        gr=0
        sulprus =0
        for i in arr:
            count[i] = 1+ count.get(i,0)
            if i > len(arr):
                gr+=1
        maxi=len(arr)
        for i in range(len(arr),0,-1):
            if i not in count:
                if gr > 0:
                    gr-=1
                elif sulprus > 0:
                    sulprus-=1
                else:
                    maxi-=1
            else:
                sulprus += (count[i]-1)
        return maxi

                