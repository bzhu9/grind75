class MyQueue:
    def __init__(self):
        self.q = []
        self.s1 = []
        self.s2 = []
        self.size = 0

    def push(self, x: int) -> None:
        self.s1.append(x)
        self.size += 1

    def pop(self) -> int:
        for n in range(self.size):
            self.s2.append(self.s1.pop())
        num = self.s2.pop()
        self.size -= 1
        for n in range(self.size):
            self.s1.append(self.s2.pop())
        return num

    def peek(self) -> int:
        for n in range(self.size):
            self.s2.append(self.s1.pop())
        num = self.s2[-1]
        for n in range(self.size):
            self.s1.append(self.s2.pop())
        return num

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
