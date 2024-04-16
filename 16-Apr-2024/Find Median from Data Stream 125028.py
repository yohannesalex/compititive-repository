# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
        
        self.n = 0
        self.m = 0
    def addNum(self, num: int) -> None:
        if self.maxheap and  self.maxheap[0]*-1 < num:
            heapq.heappush(self.minheap,num)
            self.n+=1
            if self.n > self.m:
                cur = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap,-1*cur)
                self.n-=1
                self.m+=1
        else:
            heapq.heappush(self.maxheap,-1*num)
            self.m+=1
            if self.m > self.n and (self.m - self.n > 1):
                cur = -1*heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap,cur)
                self.m-=1
                self.n+=1
        
    def findMedian(self) -> float:
        if self.n > self.m:
            return self.minheap[0]
        elif self.m > self.n:
            return  -1*self.maxheap[0]
        else:
            return (self.minheap[0] + (-1*self.maxheap[0]))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()