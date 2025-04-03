class LRUCache:
    class ListNode:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        last = self.node.prev
        last.next = node
        node.prev = last
        node.next = self.node
        self.node.prev = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.track = {}  
        self.node = self.ListNode()  
        self.node.next = self.node
        self.node.prev = self.node

    def get(self, key: int) -> int:
        if key not in self.track:
            return -1
        node = self.track[key]
        val = node.val
        self._remove(node)
        self._add(node)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.track:
            node = self.track[key]
            node.val = value   
            self._remove(node)
            self._add(node)
        else:
            if len(self.track) == self.capacity:
                lru = self.node.next   
                self._remove(lru)
                del self.track[lru.key]  

            new_node = self.ListNode(key, value)  
            self.track[key] = new_node
            self._add(new_node)
