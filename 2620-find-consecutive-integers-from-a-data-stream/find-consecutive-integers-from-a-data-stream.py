class DataStream:

    def __init__(self, value: int, k: int):
       self.stream = deque()
       self.value = value
       self.k = k 
       self.index = 0
    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if self.value == num:
            self.index +=1
        else:
            self.index = 0
        if self.index >= self.k:
            return True
        return False



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)