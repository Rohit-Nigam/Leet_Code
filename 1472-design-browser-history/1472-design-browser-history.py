class Node:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr=Node(homepage)

    def visit(self, url: str) -> None:
        newnode=Node(url)
        self.curr.next=newnode
        newnode.prev=self.curr
        self.curr=newnode
    
    def back(self, steps: int) -> str:
        while(steps and self.curr.prev):
            self.curr=self.curr.prev
            steps-=1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)