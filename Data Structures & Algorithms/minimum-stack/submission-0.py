class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val)) 
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        if self.stack:
            del self.stack[-1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        
