class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        current = self.head
        count = 0
        while current:
            if index == count:
                return current.val
            current = current.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        new_node = ListNode(val)
        current = self.head
        count = 0
        while current:
            if index - 1 == count:   
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if not self.head or index < 0:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        prev = None
        while current:
            if index == count:
                if prev:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            count += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)