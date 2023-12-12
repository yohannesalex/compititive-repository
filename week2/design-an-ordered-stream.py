class OrderedStream:
    def __init__(self, n: int):
        self.n=n
        self.count={}
        for i in range(n+1):
            self.count[i] = 0
        self.pt=1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.count[idKey] = value
        res=[]
        while self.pt <= self.n and self.count[self.pt]:
            res.append(self.count[self.pt])
            self.pt+=1
            
        return res
            


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)