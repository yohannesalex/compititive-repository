class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        ways=[0]*1002
        res=[]
        for i in trips:
            ways[i[1]]+=i[0]
            ways[i[2]]-=i[0]
        k=0
        for i in ways:
            k+=i
            res.append(k)
        for i in res:
            if capacity<i:
                return False
        return True
