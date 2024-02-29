class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.que=deque()
        self.res=[]
        self.length=0

    def ping(self, t: int) -> int:
        while self.que and  t - 3000 > self.que[0]:
            self.que.popleft()
            self.length-=1
        else:
            self.que.append(t)
            self.length+=1
        return self.length
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)