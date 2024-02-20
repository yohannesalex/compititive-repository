class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0])
        tasks.reverse()
        ans=tasks[0][1]
        cur=ans
        cur-=tasks[0][0]
        for i in range(1,len(tasks)):
            if cur < tasks[i][1]:
                ans+=(tasks[i][1]-cur)
                cur = tasks[i][1]
                cur-=tasks[i][0]
            else:
                cur-=tasks[i][0]
        return ans
            

