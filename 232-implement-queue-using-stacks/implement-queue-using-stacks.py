class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.index = 0
    def push(self, x: int) -> None:
        self.stack1.append(x)
        if len(self.stack1) - self.index == 1:
            self.stack2.append(x)
    def pop(self) -> int:
        temp = self.stack2.pop()
        self.index += 1
        if self.index < len(self.stack1):
            self.stack2.append(self.stack1[self.index])
        return temp
    def peek(self) -> int:
        return self.stack2[0] if self.stack2 else self.stack1[self.index]
    def empty(self) -> bool:
        return len(self.stack1) == self.index and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()