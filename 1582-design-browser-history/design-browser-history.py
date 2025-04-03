class ListNode:
    def __init__(self, val=0):
        self.prev = None
        self.next = None
        self.val = val
class BrowserHistory:
    def __init__(self, homepage: str):
        self.browser = ListNode(homepage)
        self.pos = self.browser
    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.pos.next = node
        node.prev = self.pos
        self.pos = node 
    def back(self, steps: int) -> str:
        while steps > 0 and self.pos.prev:
            self.pos = self.pos.prev  
            steps -= 1
        return self.pos.val
    def forward(self, steps: int) -> str:
        while steps > 0 and self.pos.next:
            self.pos = self.pos.next   
            steps -= 1
        return self.pos.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)