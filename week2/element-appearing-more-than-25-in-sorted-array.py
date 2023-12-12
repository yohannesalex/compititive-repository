class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count={}
        for i in arr:
            count[i] = 1+ count.get(i,0)
        for i in count:
            if count.get(i) > len(arr)/4:
                return i