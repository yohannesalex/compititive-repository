class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*(n+1)
        for i in bookings:
            res[i[0]-1]+=i[2]
            res[i[1]]-=i[2]
        pre=[res[0]]
        for i in res[1:]:
            pre.append(i+pre[-1])
        pre.pop()
        return pre