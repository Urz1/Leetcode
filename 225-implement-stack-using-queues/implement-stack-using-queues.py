class MyStack:
    def __init__(self):
        self.queue1 = deque()   
        self.queue2 = deque()   
        self.top_element = None

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.top_element = x   
        self.queue2.clear()
        self.queue2.append(x)

    def pop(self) -> int:
        if not self.queue1:
            return None
        result = self.queue1.pop()   
        if self.queue1:   
            self.top_element = self.queue1[-1]
            self.queue2.clear()
            self.queue2.append(self.top_element)
        else:
            self.top_element = None
            self.queue2.clear()
        return result

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()