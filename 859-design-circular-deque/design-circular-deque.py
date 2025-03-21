class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.queue) == self.capacity:
            return False
        self.queue.appendleft(value)
        return True 
    def insertLast(self, value: int) -> bool:
        if len(self.queue) == self.capacity:
            return False
        self.queue.append(value)
        return True 

    def deleteFront(self) -> bool:
        if not self.queue:
            return False
        self.queue.popleft()
        return True
    def deleteLast(self) -> bool:
        if not self.queue:
            return False
        self.queue.pop()
        return True

    def getFront(self) -> int:
        if not self.queue:
            return -1
        return self.queue[0]
    def getRear(self) -> int:
        if not self.queue:
            return -1
        return self.queue[-1]
    def isEmpty(self) -> bool:
        return False if self.queue else True

    def isFull(self) -> bool:
        return len(self.queue) == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()