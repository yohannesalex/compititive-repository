# Problem: Two Best Non-Overlapping Events - https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        maxi = 0
        for item in events:
            start , end , val = item
            maxi = max(maxi , val)
        arr = []
        m = 0
        events.sort(key = lambda x:x[1])
        print(events)
        for i in events:
            m = max(m , i[2])
            arr.append([i[1], m])
        arr.sort()
        # count = defaultdict(int)
        print(arr)
        # for i in arr:
        #     count[i[0]] = max(count[i[0]], i[1])
        # print(count)
        maxi = 0
        def search(num, maxi , arr):
            
            l = 0
            r = len(arr)-1
            while l <= r:
                mid = (l + r)//2
                if arr[mid][0] >= num:
                    
                    r = mid -1
                else:
                    maxi = max(maxi,arr[mid][1] )
                    l = mid+1
                
            return maxi
        k = search(4, maxi , arr)
        print(k)
        res = 0
        for i in events:
            res = max(res , i[2] + (search(i[0], maxi , arr)))
        return res


                    

