class BrowserHistory:
    class Node:
        def __init__(self,val):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, homepage: str):
        self.head = self.Node(homepage)
        self.tail = self.Node(homepage)
        self.curPage = self.Node(homepage)
        

    def visit(self, url: str) -> None:
        newNode = self.Node(url)
        newNode.prev = self.curPage
        self.curPage.next = newNode
        self.curPage = newNode
        self.curPage.next = None
        

    def back(self, steps: int) -> str:
        cur = self.curPage
        while steps > 0 and cur.prev:
            cur = cur.prev
            steps -= 1
        self.curPage = cur
        return self.curPage.val

    def forward(self, steps: int) -> str:
        cur = self.curPage
        while steps > 0 and cur.next:
            cur = cur.next
            steps -= 1
        self.curPage = cur
        return self.curPage.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)