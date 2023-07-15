class MinStack:
    def __init__(self):
        self.mini = None    
        self.stack = []

    def push(self, val: int) -> None:
        if self.mini is None:
            self.mini = val

        if self.mini > val:
            self.mini = val
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.mini:
            if len(self.stack) != 0:
                self.mini = min(self.stack)
            else:
                self.mini = None
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()